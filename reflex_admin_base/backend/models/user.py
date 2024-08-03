import reflex as rx
from pydantic import field_validator
from sqlmodel import Field

from reflex_admin_base.backend.utils.security import hash_password


class UserBase(rx.Model):
    username: str = Field(unique=True, index=True, min_length=3, max_length=255)
    email: str = Field(unique=True, index=True)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    is_active: bool = True
    is_superuser: bool = False

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else ""


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(rx.Model):
    email = ""
    username: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=8, max_length=40)


class UserLogin(rx.Model):
    username: str = Field(min_length=0, max_length=255)
    password: str = Field(min_length=0, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    hashed_password: str


class UserPublic(UserBase): ...
