from abc import ABC, abstractmethod
from typing import List

from llm.models import Message


class ContextManager(ABC):
    def __init__(self, key: str) -> None:
        self.key = key

    @abstractmethod
    async def save(self, message: Message) -> None:
        ...

    @abstractmethod
    async def get(self) -> List[Message]:
        ...

    @abstractmethod
    async def clear(self) -> None:
        ...
