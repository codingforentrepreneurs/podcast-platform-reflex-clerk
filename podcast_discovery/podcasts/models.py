from datetime import datetime
import sqlalchemy
from sqlmodel import Field, Session, select, BigInteger
import reflex as rx




class PodcastEpisode(rx.Model, table=True):
    track_id: int = Field(index=True, sa_type=BigInteger)
    track_name: str
    episode_url: str | None = Field(default=None)
    release_date: datetime | None = Field(default=None)
    collection_name: str | None = Field(default=None) # podcast show name
    collection_id: int = Field(index=True) # podcast show id
    description: str | None = None
    artwork_url_600: str | None = Field(default=None)
    user_interactions: int = Field(default=0)
    last_user_interaction: datetime | None = Field(default=None)
    
    @classmethod
    def update_or_create(cls, session: Session, defaults=None, **kwargs):
        track_id = kwargs.get('track_id')
        if not track_id:
            raise ValueError("track is required for update_or_create")
        if defaults is None:
            defaults = {}
        query = select(PodcastEpisode).where(PodcastEpisode.track_id == track_id)
        instance = session.exec(query).first()
        created = False

        if instance is None:
            print("Creating podcast episode")
            create_data = {**defaults, **kwargs}
            instance = PodcastEpisode(**create_data)
            session.add(instance)
            created = True
        else:
            print("updating podcast episode")
            update_data = {**defaults, **kwargs}
            for k, v in update_data.items():
                setattr(instance, k, v)
            session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance, created
    
    
    def increment_interaction(self, session: Session):
        self.user_interactions += 1
        self.last_user_interaction = datetime.now()
        session.add(self)
        session.commit()
        session.refresh(self)
        return self
    

class PodcastLike(rx.Model, table=True):
    user_id: str = Field(default=None, index=True)
    episode_id: int = Field(foreign_key="podcastepisode.id", index=True)
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )

    __table_args__ = (
        sqlalchemy.UniqueConstraint('user_id', 'episode_id', name='unique_user_episode_like'),
    )

    @classmethod
    def toggle_like(cls, session: Session, user_id: str, episode_id: int) -> tuple[bool, "PodcastLike | None"]:
        query = select(PodcastLike).where(
            PodcastLike.user_id == user_id,
            PodcastLike.episode_id == episode_id
        )
        existing_like = session.exec(query).first()
        
        if existing_like:
            session.delete(existing_like)
            session.commit()
            return False, None
        
        new_like = PodcastLike(user_id=user_id, episode_id=episode_id)
        session.add(new_like)
        session.commit()
        session.refresh(new_like)
        return True, new_like

    @classmethod
    def is_liked_by_user(PodcastLike, session: Session, user_id: str, episode_id: int) -> bool:
        """Check if a specific episode is liked by a user"""
        query = select(PodcastLike).where(
            PodcastLike.user_id == user_id,
            PodcastLike.episode_id == episode_id
        )
        return session.exec(query).first() is not None