import reflex as rx
from podcast_discovery import ui

from podcast_discovery.pages.layout import page_layout

from podcast_discovery.discovery.table import discovery_table

@rx.page("/discovery")
def discovery_page() -> rx.Component:
    return page_layout(
        discovery_table(),
        title="discovery Page"
    )