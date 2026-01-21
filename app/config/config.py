from pydantic_settings import BaseSettings, SettingsConfigDict


# app configuration object definition
class AppConfig(BaseSettings):

    DEBUG: bool = False

    BOT_TOKEN: str

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    # DSN factory for postgres DSN
    @property
    def postgres_dsn(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )
