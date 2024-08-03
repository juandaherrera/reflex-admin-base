"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from reflex_admin_base.frontend.pages import index
from reflex_admin_base.frontend.styles.styles import BASE_STYLE
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


app = rx.App(style=BASE_STYLE)
