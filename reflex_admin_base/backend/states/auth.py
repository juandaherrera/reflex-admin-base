import reflex as rx
from sqlmodel import select

from reflex_admin_base.backend.models.user import User, UserLogin, UserPublic
from reflex_admin_base.backend.utils.security import verify_password


class AuthState(rx.State):
    """The authentication state for sign up and login page."""

    user_login: UserLogin = UserLogin(username="", password="")
    user: UserPublic | None = None

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.user_login.username)
            ).first()
            if user and verify_password(self.user_login.password, user.hashed_password):
                self.user = UserPublic.from_orm(user)
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password.")
