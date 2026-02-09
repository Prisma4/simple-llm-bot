from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.texts import Texts


class ReplyKeyboards:
    @staticmethod
    def new_request_keyboard():
        keyboard = [
            [KeyboardButton(text=Texts.NEW_REQUEST)]
        ]
        return ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True
        )
