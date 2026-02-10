import logging
from aiogram import types, Router
from aiogram.filters import Command

from bot.keyboards.reply_keyboards import ReplyKeyboards
from bot.llm_manager import llm_manager
from bot.texts import Texts

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: types.Message):
    try:
        await llm_manager.clear_context(str(message.from_user.id))

        await message.answer(
            text=Texts.START_TEXT,
            reply_markup=ReplyKeyboards.new_request_keyboard()
        )
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)


@router.message(Command("help"))
async def get_help(message: types.Message):
    await message.answer(text=Texts.HELP_TEXT)
