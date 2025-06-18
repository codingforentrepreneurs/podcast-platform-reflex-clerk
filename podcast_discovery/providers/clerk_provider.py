import os
import reflex as rx
import reflex_clerk_api as reclerk

my_clerk_provider_args = dict(
        publishable_key=os.environ["CLERK_PUBLIC_KEY"],
        secret_key=os.environ["CLERK_SECRET_KEY"],
        register_user_state=True,
)

def my_clerk_provider(child:rx.Component) -> rx.Component:
    return reclerk.clerk_provider(
        rx.fragment(
            child
        ),
       **my_clerk_provider_args
    )