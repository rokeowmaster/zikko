import reflex as rx
from ..components.navbar import navbar


@rx.page(route="/")
def home() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar(),
        )
    
