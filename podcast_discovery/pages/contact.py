import reflex as rx

@rx.page("/contact")
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
    )