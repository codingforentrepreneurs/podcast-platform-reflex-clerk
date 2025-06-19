import reflex as rx
import reflex_clerk_api as reclerk

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def mobile_navbar_link(url:str):
    return rx.redirect(url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Podcast Discovery", size="7", weight="bold",
                        on_click=lambda: mobile_navbar_link("/")
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Discover", "/discovery"),
                    navbar_link("About", "/about"),
                    navbar_link("Pricing", "/pricing"),
                    navbar_link("Contact", "/contact"),
                    rx.fragment(
                        reclerk.signed_out(
                            rx.link(rx.button("Login", variant="outline"), href='/login'),
                            rx.link(rx.button("Sign up"), href='/signup'),
                        )
                    ), 
                    rx.fragment(
                        reclerk.signed_in(
                            rx.link(rx.button("Logout"), href='/logout'),
                        )
                    ),
                    justify="end",
                    spacing="3",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Podcast Discovery", size="6", weight="bold",
                        on_click=lambda: mobile_navbar_link("/")
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=lambda: mobile_navbar_link("/")),
                        rx.menu.item("About", on_click=lambda: mobile_navbar_link("/about")),
                        rx.menu.item("Pricing", on_click=lambda: mobile_navbar_link("/pricing")),
                        rx.menu.item("Contact", on_click=lambda: mobile_navbar_link("/contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )