from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str

    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"
    openai_api_url: str = "https://api.openai.com/v1/chat/completions"
