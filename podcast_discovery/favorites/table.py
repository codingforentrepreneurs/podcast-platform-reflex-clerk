import reflex as rx

from podcast_discovery.favorites.state import FavoritesState
from podcast_discovery.podcasts.table import podcast_search_results_table_row

def favorite_rows() -> rx.Component:
    return rx.cond(
        FavoritesState.count > 0,
        rx.foreach(
            FavoritesState.episodes,
            podcast_search_results_table_row
        ),
        "No episodes are liked"
    )


def favorites_table() -> rx.Component:

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Track Name"),
                rx.table.column_header_cell("Audio"),
                rx.table.column_header_cell("Release date"),
                rx.table.column_header_cell("Podcast Name"),
            ),
        ),
        rx.table.body(
            favorite_rows(),
            on_mount=FavoritesState.handle_on_mount
        ),
        width="100%",
)