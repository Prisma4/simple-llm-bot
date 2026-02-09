from typing import List

from openai import AsyncOpenAI, OpenAIError
from openai.types.chat import ChatCompletionMessageParam

from llm.llm_interface.base import AbstractLLMInterface
from llm.models import Message
from settings import Settings


class OpenAILLMInterface(AbstractLLMInterface):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = AsyncOpenAI(api_key=self.settings.openai_api_key)

    async def send_message(self, context: List[Message]) -> str:
        messages: List[ChatCompletionMessageParam] = [
            {"role": "system", "content": self.settings.system_prompt},
            *[{"role": m.role.value, "content": m.content} for m in context],
        ]

        try:
            response = await self.client.chat.completions.create(
                model=self.settings.openai_model,
                messages=messages,
            )
            content = response.choices[0].message.content or ""
            return content.strip()

        except OpenAIError as e:
            raise RuntimeError(f"OpenAI error: {e.type or 'unknown'}: {e.message}") from e

        except Exception as e:
            raise RuntimeError("Failed to call OpenAI API") from e
