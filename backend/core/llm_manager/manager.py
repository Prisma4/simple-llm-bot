from typing import List

from core.context_manager.base import AbstractMessageContextManager
from core.llm.llm_interface.base import AbstractLLMInterface
from core.llm.models import Message, MessageRole


class LLMManager:
    def __init__(
            self,
            context_manager: AbstractMessageContextManager,
            llm_interface: AbstractLLMInterface,
    ):
        self.context_manager = context_manager
        self.llm_interface = llm_interface

    def _form_message(self, role: MessageRole, content: str) -> Message:
        return Message(
            role=role,
            content=content,
        )

    async def send_message_to_llm(
            self,
            user_id: int,
            message: str
    ) -> str:
        new_message = self._form_message(
            role=MessageRole.USER,
            content=message
        )
        await self.context_manager.save_message(str(user_id), new_message)
        context: List[Message] = await self.context_manager.get_context(str(user_id))
        response: str = await self.llm_interface.send_message(context)
        new_response = self._form_message(
            role=MessageRole.ASSISTANT,
            content=response
        )
        await self.context_manager.save_message(new_response)
        return response

    async def clear_context(
            self,
            user_id: int
    ):
        await self.context_manager.clear_context(str(user_id))

