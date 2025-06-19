from typing import List, Any
import reflex as rx
from podcast_discovery import helpers

from .models import PodcastEpisode
from .schemas import PodcastEpisodeSchema, PodcastEpisodeRawAPISchema

# key_mapping = {
#     "trackName": "Title"
# }

class PodcastSearchState(rx.State):
    raw_results: List[dict] | None = None
    results: List[PodcastEpisodeSchema] | None = None
    columns: List[str] = []
    query: str = ""
    loading: bool = False

    @rx.event
    def handle_search(self, form_data):
        query = form_data.get('query')
        self.query = query
        self.results = None
        self.loading = True
        api_results = helpers.podcast_search(query, limit=100, attribute="descriptionTerm", sort_by_date=True)
        self.raw_results = api_results
        if len(api_results) > 0:
            print(api_results[0].keys())
            final_results = []
            for x in api_results:
                valid_data = PodcastEpisodeRawAPISchema.model_validate(x)
                final_data = PodcastEpisodeSchema(**valid_data.model_dump())
                final_results.append(final_data)
            self.results = final_results
            # self.columns = [key_mapping.get(y) for y in api_results[0].keys()]
        self.loading = False
        
        # call the search api


class PodcastEpisodeState(rx.State):

    @rx.event
    def user_did_interact(self, podcast: PodcastEpisodeSchema):
        print(f"User did interact", podcast.track_name, podcast.track_id)
        track_id = podcast.track_id
        defaults={
            "track_name": podcast.track_name,
            "episode_url": podcast.episode_url,
            "release_date": podcast.release_date,
            "collection_name": podcast.collection_name,
            "collection_id": podcast.collection_id,
            "description": podcast.description,
            "artwork_url_600": podcast.artwork_url_600,
        }
        with rx.session() as session:
            print("Update or create PodcastEpisode")
            instance, _ = PodcastEpisode.update_or_create(session, 
                                            track_id=track_id, 
                                            defaults=defaults)
            instance.increment_interaction(session)
            print('instance', instance.user_interactions)
            # PodcastEpisode