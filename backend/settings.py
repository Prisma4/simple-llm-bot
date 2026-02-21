from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"
    system_prompt: str = ""
    allowed_users_ids: str = ""

    redis_url: Optional[str]


MAX_BOT_MESSAGE_LENGTH = 3800  # max telegram message length is 4096, but it's better to not hit the limit if possible
