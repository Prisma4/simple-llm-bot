from abc import ABC, abstractmethod
from typing import List

from core.llm.models import Message


class AbstractMessageContextManager(ABC):
    @abstractmethod
    async def save_message(self, key: str, message: Message) -> None:
        ...

    @abstractmethod
    async def get_context(self, key: str) -> List[Message]:
        ...

    @abstractmethod
    async def clear_context(self, key: str) -> None:
        ...
