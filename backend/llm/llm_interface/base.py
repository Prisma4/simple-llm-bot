from abc import ABC, abstractmethod


class AbstractLLMInterface(ABC):
    @abstractmethod
    async def send_message(self, message_text: str) -> str:
        pass
