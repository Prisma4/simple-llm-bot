import logging

from aiogram import types, Router, F
from bot.llm_manager import llm_manager
from bot.texts import Texts

router = Router()

logger = logging.getLogger(__name__)


@router.message(F.text == Texts.NEW_REQUEST)
async def handle_new_request(message: types.Message) -> None:
    try:
        await llm_manager.clear_context(message.from_user.id)
        await message.answer(Texts.CONTEXT_CLEAR_SUCCESS)
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)


@router.message()
async def handle_message(message: types.Message) -> None:
    try:
        response = await llm_manager.send_message_with_context(message.from_user.id, message.text)
        await message.answer(response)
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)
