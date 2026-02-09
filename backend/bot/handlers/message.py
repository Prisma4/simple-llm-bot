from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.context_manager.fsm import FSMContextManager
from bot.states import BotStates
from bot.texts import Texts
from llm.llm_interface.open_ai import OpenAILLMInterface
from settings import Settings

router = Router()


@router.message(F.text == Texts.NEW_REQUEST)
async def clear_context(message: types.Message, state: FSMContext):
    context_manager = FSMContextManager("user_messages", state)
    await context_manager.clear()
    await message.answer(text=Texts.CONTEXT_CLEAR_SUCCESS)


@router.message()
async def llm_request(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.main_state)  # ensuring state is set

    context_manager = FSMContextManager("user_messages", state)
    await context_manager.save(message.text)
    all_messages = await context_manager.get()

    settings = Settings()
    llm_interface = OpenAILLMInterface(settings)

    response_from_llm = await llm_interface.send_message(", ".join(all_messages))

    await message.answer(text=response_from_llm)
