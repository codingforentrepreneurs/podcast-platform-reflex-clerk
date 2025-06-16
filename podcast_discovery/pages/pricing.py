import reflex as rx
from podcast_discovery import ui

from podcast_discovery.pages.layout import page_layout

@rx.page("/pricing")
def pricing_page() -> rx.Component:
    return page_layout(
        rx.text("This is my pricing page, I'll add to it later"),
        title="Pricing Page"
    )