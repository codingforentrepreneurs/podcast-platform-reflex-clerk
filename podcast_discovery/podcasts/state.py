from typing import List, Any
import reflex as rx
from podcast_discovery import helpers

from .schemas import PodcastEpisodeSchema

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
            self.results = [PodcastEpisodeSchema(**x) for x in api_results]
            # self.columns = [key_mapping.get(y) for y in api_results[0].keys()]
        self.loading = False
        
        # call the search api
