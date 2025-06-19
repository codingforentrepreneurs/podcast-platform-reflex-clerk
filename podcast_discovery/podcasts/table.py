import reflex as rx

from .state import PodcastSearchState

def search_table_row(data:dict) -> rx.Component:

    return rx.table.row(
                rx.table.row_header_cell(data.get("title")),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Developer"),
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
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
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