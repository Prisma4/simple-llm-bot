import asyncio
import logging
from aiogram import Bot, Dispatcher

from bot.handlers import start, message
from bot.middlewares.auth import IsAllowedUserMiddleware
from settings import Settings

settings = Settings()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.bot_token)

dp = Dispatcher()
dp.include_router(start.router)
dp.include_router(message.router)

dp.message.middleware(
    IsAllowedUserMiddleware(
        allowed_users_ids=[int(v.strip()) for v in settings.allowed_users_ids.split(",")],
        silent=True
    )
)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
