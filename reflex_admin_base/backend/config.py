from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database URL
    DATABASE_URL: str = "sqlite:///reflex_admin.db"

    ENVIRONMENT: str = "development"

    # Backend
    SECRET_KEY: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_PASSWORD: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
