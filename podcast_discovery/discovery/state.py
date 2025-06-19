from typing import List, Any
import reflex as rx
from sqlmodel import select, func

from podcast_discovery.podcasts.models import PodcastEpisode, PodcastLike
from podcast_discovery.favorites.state import UserPodcastLikeState

class DiscoveryState(rx.State):
    episodes: List[PodcastEpisode] = []
    count: int = 0
    limit: int = 20

    @rx.event
    async def handle_on_mount(self):
        user_like_state = await self.get_state(UserPodcastLikeState)
        await user_like_state.handle_on_mount()
        with rx.session() as session:
            query = select(
                PodcastEpisode
            ).join(
                PodcastLike,
                PodcastLike.episode_id == PodcastEpisode.id
            ).group_by(
                PodcastEpisode.id
            ).having(
                func.count(PodcastLike.id) > 0
            ).order_by(
                func.random()
            ).limit(self.limit)
            self.episodes = session.exec(query).fetchall()
            self.count = len(self.episodes)