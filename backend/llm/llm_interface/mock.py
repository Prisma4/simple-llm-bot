import random

from llm.llm_interface.base import AbstractLLMInterface


class MockLLMInterface(AbstractLLMInterface):
    async def send_message(self, message_text: str) -> str:
        mock_answer = random.choice(message_text.split(","))
        return mock_answer
