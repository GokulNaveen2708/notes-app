from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Where the database lives. Default is fine for local dev;
    # in production this comes from the environment.
    database_url: str = "sqlite:///./notes.db"
    sqs_queue_url: str = ""

    # App metadata, also overridable from the environment.
    app_name: str = "Notes API"
    debug: bool = False


# One shared, importable instance. The rest of the app imports THIS,
# never re-reads the environment itself.
settings = Settings()