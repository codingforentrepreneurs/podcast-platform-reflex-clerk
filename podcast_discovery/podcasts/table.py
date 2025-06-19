import reflex as rx


def search_table_row(data:dict):

    return rx.table.row(
                rx.table.row_header_cell(data.get("title")),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Developer"),
            )


def search_results_table():

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                [{"id": 123, "title": "My new title"}, {"id": 123, "title": "My new title"}],
                search_table_row
            )
        ),
        width="100%",
)