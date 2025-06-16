import reflex as rx
from podcast_discovery import ui

@rx.page("/about")
def about_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            ui.page_heading("About"),
            rx.link(
                rx.button("Home"),
                href="/",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )