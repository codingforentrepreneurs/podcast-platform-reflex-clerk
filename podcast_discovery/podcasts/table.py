import reflex as rx

from .players import podcast_audio_player, podcast_video_player
from .schemas import PodcastEpisodeSchema
from .state import PodcastSearchState

def search_table_row(podcast:PodcastEpisodeSchema) -> rx.Component:
    audio_el = podcast_audio_player(podcast.episode_url)
    return rx.table.row(
                rx.table.row_header_cell(podcast.track_name),
                rx.table.cell(audio_el),
                rx.table.cell(podcast.release_date),
                rx.table.cell(podcast.collection_name),
            )


def search_results_rows() -> rx.Component:
    query_label = rx.cond(
        PodcastSearchState.query, 
        f"No results found for query {PodcastSearchState.query}",
        "Search for a podcast episode"
        )

    return rx.cond(
                PodcastSearchState.results,
                rx.foreach(
                    PodcastSearchState.results,
                    search_table_row
                ),
                query_label
            )


def search_results_table() -> rx.Component:

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
            rx.cond(
                PodcastSearchState.loading,
                rx.spinner(),
                search_results_rows() 
            )
            
        ),
        width="100%",
)