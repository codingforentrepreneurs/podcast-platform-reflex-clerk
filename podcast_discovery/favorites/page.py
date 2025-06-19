import reflex as rx
from podcast_discovery import ui

from podcast_discovery.pages.layout import page_layout

from podcast_discovery.favorites.table import favorites_table

@rx.page("/favorites")
def favorites_page() -> rx.Component:
    return page_layout(
        favorites_table(),
        title="Favorites Page"
    )