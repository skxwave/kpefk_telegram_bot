import asyncio

from aiogram import Dispatcher, Bot

from bot.handlers import commands_router
from core.config import settings


async def main():
    bot = Bot(token=settings.api.telegram_key)
    dp = Dispatcher()
    dp.include_routers(
        commands_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
