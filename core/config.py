from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseModel):
    url: str


class ApiKeys(BaseModel):
    telegram_key: str


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        env_prefix="BOT__",
        env_nested_delimiter="__",
    )
    api: ApiKeys
    db: Database


settings = Config()
