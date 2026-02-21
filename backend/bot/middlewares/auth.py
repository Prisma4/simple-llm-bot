from typing import Callable, Dict, Any, Awaitable, List

from aiogram import BaseMiddleware, types
from aiogram.types import Message


class IsAllowedUserMiddleware(BaseMiddleware):
    def __init__(
            self,
            allowed_users_ids: List[int],
            silent: bool = False,
            error_text: str = "You're not in the allowed users list.",
    ):
        self.allowed_users_ids = allowed_users_ids
        self.silent = silent
        self.error_text = error_text

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, Message) or not self.allowed_users_ids:
            return await handler(event, data)

        user_id = event.from_user.id

        if user_id in self.allowed_users_ids:
            return await handler(event, data)

        if self.silent:
            return None

        try:
            await event.answer(self.error_text)
        except Exception:
            pass

        return None
