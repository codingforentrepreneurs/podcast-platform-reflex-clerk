import reflex as rx

from .state import PodcastSearchState

def search_table_row(data:dict) -> rx.Component:
    """
    ['episodeUrl', 'collectionViewUrl', 'trackViewUrl', 
    'artworkUrl60', 'trackTimeMillis', 'contentAdvisoryRating', 
    'previewUrl', 'artistIds', 'genres', 
    'episodeGuid', 'releaseDate', 'trackId', 
    'trackName', 'shortDescription', 'feedUrl', 
    'closedCaptioning', 'collectionId', 'collectionName', 
    'kind', 'wrapperType', 'description', 'country', 
    'artworkUrl600', 'episodeFileExtension', 
    'episodeContentType', 'artworkUrl160']
    
    """
    return rx.table.row(
                rx.table.row_header_cell(data.get("trackName")),
                rx.table.cell(data.get("episodeUrl")),
                rx.table.cell(data.get("releaseDate")),
                rx.table.cell(data.get("collectionName")),
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