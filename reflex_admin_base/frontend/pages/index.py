import reflex as rx

from reflex_admin_base.frontend.components.shared import navbar
from reflex_admin_base.frontend.styles.colors import Color, TextColor
from reflex_admin_base.frontend.styles.styles import GENERAL_PAGE_PADDING_X


@rx.page(
    route="/",
    title="Admin Base 🚀",
    # description=const.INDEX_DESCRIPTION,
    # image=const.INDEX_PREVIEW,
    # meta=const.INDEX_META,
)
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            min_height="80vh",
            width="100%",
            padding_x=GENERAL_PAGE_PADDING_X,
        ),
        spacing="5",
        min_height="100vh",
        width="100%",
        bg=Color.BACKGROUND.value,
    )
