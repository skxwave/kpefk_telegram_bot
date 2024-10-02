import asyncio

from aiogram import Dispatcher, Bot

import bot.handlers as rt
from core.config import settings


async def main():
    bot = Bot(token=settings.api.telegram_key)
    dp = Dispatcher()
    dp.include_routers(
        rt.commands_router,
        rt.schedule_router,
        rt.group_router,
        rt.admin_menu_router,
        rt.admin_schedule_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
