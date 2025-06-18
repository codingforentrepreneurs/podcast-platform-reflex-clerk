import reflex as rx
from podcast_discovery import ui
from podcast_discovery.layout import root_layout
from podcast_discovery.ui.nav import navbar

def page_layout(children: rx.Component, title: str =None) -> rx.Component:
    return root_layout(
            rx.container(
            rx.vstack(
                ui.page_heading(title),
                rx.box(
                    children,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
           size="4"
        )
    )