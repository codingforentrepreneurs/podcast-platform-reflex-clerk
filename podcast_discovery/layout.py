import reflex as rx

def root_layout(child:rx.Component, *args, **kwargs):

    return rx.container( # do not render
        rx.fragment(child),
        rx.logo(),
        width="100%",
        id='my-root-layout'
    )