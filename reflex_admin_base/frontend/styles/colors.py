from enum import Enum

import reflex as rx


class Color(Enum):
    PRIMARY = rx.color("indigo", 9)
    BACKGROUND = rx.color("mauve", 2)
    NAVBAR = rx.color("mauve", 1)
    BORDERS = f"1px solid {rx.color('mauve', 4)}"


class TextColor(Enum):
    ACCENT = rx.color("mauve", 11)
    PRIMARY = rx.color("mauve", 12)
