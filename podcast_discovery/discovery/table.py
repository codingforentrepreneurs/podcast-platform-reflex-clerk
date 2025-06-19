import reflex as rx

from podcast_discovery.discovery.state import DiscoveryState
from podcast_discovery.podcasts.table import podcast_search_results_table_row

def favorite_rows() -> rx.Component:
    return rx.cond(
        DiscoveryState.count > 0,
        rx.foreach(
            DiscoveryState.episodes,
            podcast_search_results_table_row
        ),
        "No episodes to show"
    )


def discovery_table() -> rx.Component:

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
            on_mount=DiscoveryState.handle_on_mount
        ),
        width="100%",
)