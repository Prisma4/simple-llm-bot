import logging

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.context_manager.fsm import FSMContextManager
from bot.texts import Texts
from llm.llm_interface.open_ai import OpenAILLMInterface
from llm.models import Message, MessageRole
from settings import Settings

router = Router()

logger = logging.getLogger(__name__)


@router.message(F.text == Texts.NEW_REQUEST)
async def cmd_new_request(message: types.Message, state: FSMContext) -> None:
    try:
        ctx = FSMContextManager("user_messages", state)
        await ctx.clear()
        await message.answer(Texts.CONTEXT_CLEAR_SUCCESS)
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)


@router.message()
async def handle_message(message: types.Message, state: FSMContext) -> None:
    try:
        ctx = FSMContextManager("user_messages", state)

        await ctx.save(Message(role=MessageRole.USER, content=message.text))

        response = await OpenAILLMInterface(Settings()).send_message(
            await ctx.get()
        )

        await ctx.save(Message(role=MessageRole.ASSISTANT, content=response))
        await message.answer(response)
    except Exception as e:
        logger.exception(e)
        await message.answer(Texts.ERROR_TEXT)
