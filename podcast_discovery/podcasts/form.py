import reflex as rx

from .state import PodcastSearchState

def search_form() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(type='text', name='query', placeholder="Search for podcast episodes"),
            rx.button("Search podcasts", type="submit")
        ),
        on_submit=PodcastSearchState.handle_search
    )