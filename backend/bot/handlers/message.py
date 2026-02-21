import logging

from aiogram import types, Router, F

from bot.llm_manager import llm_manager
from bot.texts import Texts
from bot.utils import split_message, message_photo_to_base64
from settings import MAX_BOT_MESSAGE_LENGTH

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
        images_b64 = await message_photo_to_base64(message)

        text = message.text or message.caption
        image = [images_b64] if images_b64 else None

        response = await llm_manager.send_request_with_context(
            message.from_user.id,
            text,
            image
        )

        messages = split_message(response, MAX_BOT_MESSAGE_LENGTH)
        for m in messages:
            await message.answer(m)
            logger.info(f'Message with len {len(m)} sent to {message.from_user.id}')

    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)
