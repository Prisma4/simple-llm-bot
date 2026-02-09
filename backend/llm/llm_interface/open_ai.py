import openai

from llm.llm_interface.base import AbstractLLMInterface
from settings import Settings


class OpenAILLMInterface(AbstractLLMInterface):
    def __init__(self, settings: Settings):
        self.settings = settings
        openai.api_key = self.settings.openai_api_key

    async def send_message(self, message_text: str) -> str:
        try:
            response = await openai.ChatCompletion.create(
                model=self.settings.openai_model,
                messages=[{"role": "user", "content": message_text}]
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error calling API: {e}"
