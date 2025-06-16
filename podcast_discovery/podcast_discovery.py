"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


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
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.title, size="9"),
            rx.text(
                "Count: ",
                State.click_count,
                size="5",
            ),
            rx.button("Click me", on_click=State.toggle_title),
            rx.link(
                rx.button("Contact us!"),
                href="/contact",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


def contact_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Contact", size="9"),
            rx.link(
                rx.button("Home"),
                href="/",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index, route='/')
app.add_page(contact_page, route="/contact")
