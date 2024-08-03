import reflex as rx

from reflex_admin_base.backend.config import settings

config = rx.Config(
    app_name="reflex_admin_base",
    db_url=settings.DATABASE_URL,
)
