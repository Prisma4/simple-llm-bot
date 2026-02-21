from typing import List, Optional, Any

from core.context_manager.base import AbstractMessageContextManager
from core.llm.llm_interface.base import AbstractLLMInterface
from core.llm.models import Message, MessageRole


class LLMManager:
    """
    Class for an external interaction with LLM service.
    Can be initiated in any environment, e.g. bots, backend e.t.c.
    """
    def __init__(
            self,
            context_manager: AbstractMessageContextManager,
            llm_interface: AbstractLLMInterface,
    ):
        self.context_manager = context_manager
        self.llm_interface = llm_interface

    def _form_message(
            self,
            role: MessageRole,
            content: Optional[str] = None,
            images_b64: Optional[List[str]] = None,
            image_mime: str = "image/jpeg",
    ) -> Message:
        parts: List[dict[str, Any]] = []
        if content:
            parts.append({"type": "text", "text": content})

        for b64 in (images_b64 or []):
            parts.append({
                "type": "image_url",
                "image_url": {"url": f"data:{image_mime};base64,{b64}"},
            })

        return Message(role=role, content=parts)

    async def send_request_with_context(
            self,
            user_id: int,
            message: Optional[str] = None,
            images_b64: Optional[List[str]] = None
    ) -> str:
        new_message = self._form_message(
            role=MessageRole.USER,
            content=message,
            images_b64=images_b64,
        )
        await self.context_manager.save_message(str(user_id), new_message)

        context: List[Message] = await self.context_manager.get_context(str(user_id))
        response: str = await self.llm_interface.send_message(context)
        new_response = self._form_message(
            role=MessageRole.ASSISTANT,
            content=response
        )
        await self.context_manager.save_message(str(user_id), new_response)

        return response

    async def clear_context(
            self,
            user_id: int
    ):
        await self.context_manager.clear_context(str(user_id))
