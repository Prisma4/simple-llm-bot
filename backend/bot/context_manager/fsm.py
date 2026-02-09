from aiogram.fsm.context import FSMContext

from bot.context_manager.base import ContextManager


class FSMContextManager(ContextManager):
    def __init__(self, key: str, state: FSMContext) -> None:
        super().__init__(key)
        self.state = state

    async def save(self, data: str) -> None:
        data_list = await self.get()
        data_list.append(data)
        await self.state.update_data({self.key: data_list})

    async def get(self) -> list:
        data = await self.state.get_data()
        return data.get(self.key, [])

    async def clear(self) -> None:
        await self.state.update_data({self.key: []})
