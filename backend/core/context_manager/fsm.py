from typing import List

from aiogram.fsm.context import FSMContext

from core.context_manager.base import AbstractMessageContextManager
from core.llm.models import Message


class FSMMessageContextManager(AbstractMessageContextManager):
    def __init__(self, state: FSMContext) -> None:
        self.state = state

    async def save_message(self, key: int, message: Message) -> None:
        state = self.state
        if not state:
            return

        history = await self.get_context(key)
        history.append(message)
        await state.update_data({str(key): history})

    async def get_context(self, key: int) -> List[Message]:
        state = self.state
        if state:
            data = await state.get_data()
            return data.get(str(key), [])
        else:
            return []

    async def clear_context(self, key: int) -> None:
        state = self.state
        if state:
            await state.update_data({str(key): []})
        else:
            pass
