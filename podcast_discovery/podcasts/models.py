from datetime import datetime
from sqlmodel import Field
import reflex as rx


class PodcastEpisode(rx.Model, table=True):
    track_id: int = Field(index=True)
    track_name: str
    episode_url: str | None = Field(default=None)
    release_date: datetime | None = Field(default=None)
    collection_name: str | None = Field(default=None) # podcast show name
    collection_id: int = Field(index=True) # podcast show id
    description: str | None = None
    artwork_url_600: str | None = Field(default=None)