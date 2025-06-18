from typing import List, Any
import reflex as rx
from podcast_discovery import helpers

class PodcastSearchState(rx.State):
    results: List[dict] | None = None
    query: str = ""

    @rx.event
    def handle_search(self, form_data):
        query = form_data.get('query')
        api_results = helpers.podcast_search(query, limit=5, attribute="titleTerm")
        if len(api_results) > 0:
            print(api_results[0].keys())
        self.results = api_results
        # call the search api




def search_form() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(type='text', name='query', placeholder="Search for podcast episodes"),
            rx.button("Search podcasts", type="submit")
        ),
        on_submit=PodcastSearchState.handle_search
    )