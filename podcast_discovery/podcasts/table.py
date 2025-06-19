import reflex as rx

from podcast_discovery.favorites.state import UserPodcastLikeState

from podcast_discovery.podcasts.models import PodcastEpisode

from .players import podcast_audio_player, podcast_video_player
from .schemas import PodcastEpisodeSchema
from .state import PodcastSearchState, PodcastEpisodeState 


def podcast_search_results_table_row(podcast:PodcastEpisodeSchema | PodcastEpisode) -> rx.Component:
    audio_el = podcast_audio_player(podcast.episode_url)
    # "item " in []
    like_button = rx.cond(
        UserPodcastLikeState.liked_podcast_track_ids.contains(podcast.track_id), 
        rx.button("Liked",  on_click=PodcastEpisodeState.user_did_toggle_like(podcast=podcast)),
        rx.button("Like", variant='outline', on_click=PodcastEpisodeState.user_did_toggle_like(podcast=podcast)) 
    )
    return rx.table.row(
                rx.table.row_header_cell(
                    rx.hstack(
                        like_button,
                        rx.text(podcast.track_name)
                    )
                ),
                rx.table.cell(audio_el),
                rx.table.cell(podcast.release_date, on_click=PodcastEpisodeState.user_did_interact(podcast=podcast)),
                rx.table.cell(podcast.collection_name, on_click=PodcastEpisodeState.user_did_interact(podcast=podcast)),
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
                    podcast_search_results_table_row
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
            ),
            on_mount=UserPodcastLikeState.handle_on_mount
        ),
        width="100%",
)