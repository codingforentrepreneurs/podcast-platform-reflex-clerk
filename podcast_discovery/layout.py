import reflex as rx
import reflex_clerk_api as reclerk
from podcast_discovery.ui.nav import navbar

from podcast_discovery.ui.sidebar import user_sidebar


def non_user_layout(child:rx.Component)-> rx.Component:

    return rx.container(
            navbar(),
            rx.fragment(child),
            rx.logo(),
            width="100%",
            id='my-root-layout'
        )



def user_layout(child:rx.Component)-> rx.Component:

    return rx.box(
            rx.hstack(
                user_sidebar(),
                rx.fragment(child),
            ),
            width="100%",
            id='my-root-layout'
        )


def root_layout(child:rx.Component, *args, **kwargs)-> rx.Component:

    return rx.fragment(
        reclerk.clerk_loading(
            rx.spinner(),
        ),
        reclerk.clerk_loaded(
            reclerk.signed_in(
                user_layout(child)
                
            ),
            reclerk.signed_out(
                non_user_layout(child)
            ),
        ),
    )