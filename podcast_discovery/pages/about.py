import reflex as rx
from podcast_discovery import ui

from podcast_discovery.pages.layout import page_layout

@rx.page("/about")
def about_page() -> rx.Component:
    return page_layout(
        rx.text("This is my about page, I'll add to it later"),
        title="About Page"
    )