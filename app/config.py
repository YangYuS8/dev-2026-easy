from functools import lru_cache
from urllib.parse import quote

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    postgres_user: str = "task_user"
    postgres_password: str = "task_password"
    database_host: str = "db"
    database_port: int = 5432
    database_name: str = "task_service"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        encoded_user = quote(self.postgres_user, safe="")
        encoded_password = quote(self.postgres_password, safe="")
        return (
            f"postgresql://{encoded_user}:{encoded_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
