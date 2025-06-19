from typing import List, Any
import reflex as rx
import reflex_clerk_api as reclerk
from podcast_discovery import helpers
from sqlmodel import select, func

from podcast_discovery.podcasts.models import PodcastEpisode, PodcastLike

class UserPodcastLikeState(rx.State):
    liked_podcast_track_ids: List[int] = []

    @rx.event
    async def handle_on_mount(self):
        clerk_state = await self.get_state(reclerk.ClerkState)
        user_id = clerk_state.user_id
        if not user_id:
            return 
        with rx.session() as session:
            query = select(
                PodcastEpisode.track_id
            ).join(
                PodcastLike,
                PodcastLike.episode_id == PodcastEpisode.id
            ).where(
                PodcastLike.user_id == user_id
            )
            track_ids = session.exec(query).fetchall()
            self.liked_podcast_track_ids = track_ids




class FavoritesState(rx.State):
    episodes: List[PodcastEpisode] = []
    count: int = 0

    @rx.event
    async def handle_on_mount(self):
        clerk_state = await self.get_state(reclerk.ClerkState)
        user_id = clerk_state.user_id
        if not user_id:
            return 
        user_like_state = await self.get_state(UserPodcastLikeState)
        await user_like_state.handle_on_mount()
        with rx.session() as session:
            query = select(
                PodcastEpisode
            ).join(
                PodcastLike,
                PodcastLike.episode_id == PodcastEpisode.id
            ).where(
                PodcastLike.user_id == user_id
            ).group_by(
                PodcastEpisode.id
            ).order_by(
                func.max(PodcastLike.created_at).desc()
            )
            self.episodes = session.exec(query).fetchall()
            self.count = len(self.episodes)