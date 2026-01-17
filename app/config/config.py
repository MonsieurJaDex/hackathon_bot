from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


# app configuration object definition
class AppConfig(BaseSettings):

    debug: bool = False

    bot_token: str

    postgres_dsn: PostgresDsn

    model_config = SettingsConfigDict(
        env_file="app/.env",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )
