from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"
    system_prompt: str = ""

    redis_url: Optional[str]


