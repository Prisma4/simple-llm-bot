from abc import ABC, abstractmethod
from typing import List

from core.llm.models import Message


class AbstractLLMInterface(ABC):
    """
    Abstract interface for LLM.
    Sends a message to LLM.
    """
    @abstractmethod
    async def send_message(self, context: List[Message]) -> str:
        pass
