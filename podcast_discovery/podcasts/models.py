from datetime import datetime
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