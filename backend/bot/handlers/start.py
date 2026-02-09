from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.context_manager.fsm import FSMContextManager
from bot.keyboards.reply_keyboards import ReplyKeyboards
from bot.states import BotStates
from bot.texts import Texts

router = Router()


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.main_state)
    context_manager = FSMContextManager("user_messages", state)
    await context_manager.clear()
    await message.answer(
        text=Texts.START_TEXT,
        reply_markup=ReplyKeyboards.new_request_keyboard()
    )


@router.message(Command("help"))
async def get_help(message: types.Message, state: FSMContext):
    await message.answer(text=Texts.HELP_TEXT)
