import logging

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.context_manager.fsm import FSMContextManager
from bot.keyboards.reply_keyboards import ReplyKeyboards
from bot.states import BotStates
from bot.texts import Texts

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    try:
        await state.set_state(BotStates.main_state)
        ctx = FSMContextManager("user_messages", state)
        await ctx.clear()
        await message.answer(
            text=Texts.START_TEXT,
            reply_markup=ReplyKeyboards.new_request_keyboard()
        )
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)


@router.message(Command("help"))
async def get_help(message: types.Message, state: FSMContext):
    await message.answer(text=Texts.HELP_TEXT)
