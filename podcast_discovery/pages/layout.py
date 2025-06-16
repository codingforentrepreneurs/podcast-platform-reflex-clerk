import reflex as rx
from podcast_discovery import ui
from podcast_discovery.layout import root_layout

def page_layout(children: rx.Component, title: str =None) -> rx.Component:
    return root_layout(
            rx.container(
            rx.vstack(
                ui.page_heading(title),
                rx.box(
                    children,
                ),
                rx.link(
                    rx.button("Home"),
                    href="/",
                    is_external=False,
                ),
                rx.link(
                    rx.button("Contact"),
                    href="/contact",
                    is_external=False,
                ),
                rx.link(
                    rx.button("About"),
                    href="/about",
                    is_external=False,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        )
    )