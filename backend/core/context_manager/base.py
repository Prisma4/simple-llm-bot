from abc import ABC, abstractmethod
from typing import List

from core.llm.models import Message


class AbstractMessageContextManager(ABC):
    """
    Abstract class for message context managers.
    Message context manager is an entity which saves user's message history, provides and clears it.
    """
    @abstractmethod
    async def save_message(self, key: str, message: Message) -> None:
        ...

    @abstractmethod
    async def get_context(self, key: str) -> List[Message]:
        ...

    @abstractmethod
    async def clear_context(self, key: str) -> None:
        ...
