"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_clerk_api as reclerk
from podcast_discovery.providers import my_clerk_provider_args
from podcast_discovery.contact import * # noqa -> importing pages to use them
from podcast_discovery.pages import * # noqa -> importing pages to use them
from podcast_discovery.discovery.page import * # noqa -> importing pages to use them
from podcast_discovery.favorites.page import * # noqa -> importing pages to use them
from podcast_discovery import auth

from rxconfig import config
from podcast_discovery.layout import root_layout
from podcast_discovery.podcasts.form import search_form
from podcast_discovery.podcasts.table import search_results_table


class State(rx.State):
    """The app state."""
    title: str = "Like"
    og_title:  str = "Like"
    new_title: str = "Liked"
    click_count: int = 0

    @rx.event # event handler
    def toggle_title(self):
        if self.title == self.og_title:
            self.title = self.new_title
        else:
            self.title = self.og_title
        self.click_count += 1
        print("Something happend")
        


def index() -> rx.Component:
    # Welcome Page (Index)
    welcome_message = rx.cond(
        reclerk.ClerkState.is_signed_in, 
        f"Welcome {reclerk.ClerkUser.first_name}!", 
        State.title)
     # bool
    return root_layout(
            rx.container(

                rx.vstack(
                    rx.heading(welcome_message, size="9"),
                    search_form(),
                    search_results_table(),
                    spacing="5",
                    justify="center",
                    min_height="85vh",
                ),

            size="4"

        )
    )



app = rx.App()
reclerk.wrap_app(app, **my_clerk_provider_args)
app.add_page(index, route='/')
app.add_page(auth.login_page, route='/login')
app.add_page(auth.signup_page, route='/signup')
app.add_page(auth.logout_page, route='/logout')
