from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://ontology:ontology@localhost:5432/ontology"
    jwt_secret: str = "local-only-change-this-secret-at-least-32-bytes"
    jwt_access_token_minutes: int = 60
    admin_email: str = "admin@example.local"
    admin_password: str = "change-this-local-password"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
