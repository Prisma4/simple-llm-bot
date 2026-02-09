from abc import ABC, abstractmethod
from typing import List

from llm.models import Message


class AbstractLLMInterface(ABC):
    @abstractmethod
    async def send_message(self, context: List[Message]) -> str:
        pass
