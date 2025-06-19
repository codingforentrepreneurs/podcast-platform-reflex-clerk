from typing import List, Any
import reflex as rx
from podcast_discovery import helpers

class PodcastSearchState(rx.State):
    results: List[dict] | None = None
    query: str = ""
    loading: bool = False

    @rx.event
    def handle_search(self, form_data):
        query = form_data.get('query')
        self.query = query
        self.results = None
        self.loading = True
        api_results = helpers.podcast_search(query, limit=5, attribute="descriptionTerm")
        if len(api_results) > 0:
            print(api_results[0].keys())
        self.loading = False
        self.results = api_results
        # call the search api
