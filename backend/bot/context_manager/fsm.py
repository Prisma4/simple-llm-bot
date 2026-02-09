from typing import List

from aiogram.fsm.context import FSMContext

from bot.context_manager.base import ContextManager
from llm.models import Message


class FSMContextManager(ContextManager):
    def __init__(self, key: str, state: FSMContext) -> None:
        super().__init__(key)
        self.state = state

    async def save(self, message: Message) -> None:
        history = await self.get()
        history.append(message)
        await self.state.update_data({self.key: history})

    async def get(self) -> List[Message]:
        data = await self.state.get_data()
        return data.get(self.key, [])

    async def clear(self) -> None:
        await self.state.update_data({self.key: []})
