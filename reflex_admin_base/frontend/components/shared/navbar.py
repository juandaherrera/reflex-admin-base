import reflex as rx

from reflex_admin_base.backend.states import AuthState
from reflex_admin_base.frontend.styles.colors import Color, TextColor
from reflex_admin_base.frontend.styles.styles import NAVBAR_STYLE, Size, Spacing


def link_item(name: str, url: str):
    return rx.link(
        rx.center(
            rx.text(
                name,
                color=TextColor.ACCENT.value,
                font="Instrument Sans",
                style={"font-size": "16px"},
                weight="medium",
            ),
            height="100%",
        ),
        href=url,
    )


def color() -> rx.Component:
    return rx.flex(
        rx.color_mode.icon(
            light_component=rx.icon("sun", color=rx.color("mauve", 9)),
            dark_component=rx.icon("moon", color=rx.color("mauve", 9)),
        ),
        on_click=rx.style.toggle_color_mode,
        _hover={"cursor": "pointer"},
        padding="7px",
        style={
            "border_radius": "50px",
            "border": f"1px solid {rx.color('mauve', 4)}",
            "background": rx.color('mauve', 2),
            "box_shadow": "0px 3px 7px -4px rgba(21, 18, 44, 0.15)",
            "padding": "7px 12px 7px 12px",
            "align_items": "center",
        },
        border_radius="8px",
    )


def profile() -> rx.Component:
    return rx.hstack(
        rx.text(AuthState.user.first_name),
        rx.avatar(fallback="JD", size="2"),
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "AppName 🚀",
                            size=Spacing.VERY_BIG.value,
                            weight="bold",
                            color=Color.PRIMARY.value,
                        ),
                        href="/",
                    ),
                    rx.divider(
                        orientation="vertical",
                        height=Size.DEFAULT_BIG.value,
                        margin_x=Size.DEFAULT_MEDIUM.value,
                    ),
                    rx.hstack(
                        link_item("Home", "/"),
                        link_item("About", "/#"),
                        link_item("Pricing", "/#"),
                        link_item("Contact", "/#"),
                        spacing=Spacing.DEFAULT_BIG.value,
                    ),
                    align_items="center",
                ),
                color(),
                profile(),
                color=TextColor.ACCENT.value,
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "CVuilder 🚀",
                        size=Spacing.VERY_BIG.value,
                        weight="bold",
                        color=Color.PRIMARY.value,
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=NAVBAR_STYLE,
        # bg=rx.color("accent", 3),
        # padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        # width="100%",
    )
