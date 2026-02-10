from typing import List

from openai import AsyncOpenAI, OpenAIError
from openai.types.chat import ChatCompletionMessageParam

from core.llm.llm_interface.base import AbstractLLMInterface
from core.llm.models import Message


class OpenAILLMInterface(AbstractLLMInterface):
    def __init__(
            self,
            api_key: str,
            model: str,
            system_prompt: str = ""
    ):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt

    async def send_message(self, context: List[Message]) -> str:
        messages: List[ChatCompletionMessageParam] = [
            {"role": "system", "content": self.system_prompt},
            *[{"role": m.role.value, "content": m.content} for m in context],
        ]

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            content = response.choices[0].message.content or ""
            return content.strip()

        except OpenAIError as e:
            raise RuntimeError(f"OpenAI error: {e.type or 'unknown'}: {e.message}") from e

        except Exception as e:
            raise RuntimeError("Failed to call OpenAI API") from e
