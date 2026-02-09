from abc import ABC, abstractmethod


class ContextManager(ABC):
    def __init__(self, key: str) -> None:
        self.key = key

    @abstractmethod
    async def save(self, data: str) -> None:
        pass

    @abstractmethod
    async def get(self) -> list:
        pass

    @abstractmethod
    async def clear(self) -> None:
        pass
