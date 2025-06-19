from datetime import datetime
from pydantic import BaseModel, Field



class PodcastEpisodeRawAPISchema(BaseModel):
    track_id: int = Field(alias="trackId")
    track_name: str = Field(alias="trackName")
    episode_url: str = Field(alias="episodeUrl")
    release_date: datetime = Field(alias="releaseDate")
    collection_name: str = Field(alias="collectionName")
    collection_id: int = Field(alias="collectionId")
    description: str | None = None
    artwork_url_600: str | None = Field(None, alias="artworkUrl600")

    class Config:
        populate_by_alias = True
        from_attributes = True


class PodcastEpisodeSchema(BaseModel):
    track_id: int
    track_name: str
    episode_url: str
    release_date: datetime
    collection_name: str
    collection_id: int
    description: str | None = None
    artwork_url_600: str | None = None