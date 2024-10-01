from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.keyboards import get_menu
from core import db_helper

router = Router()


@router.message(Command("start", "menu"))
async def start_message(message: Message):
    user = await db_helper.find_user(int(message.from_user.id))
    if not user:
        await db_helper.create_user(
            username=message.from_user.username,
            telegram_id=message.from_user.id,
        )
    await message.answer(
        "*Menu:*",
        reply_markup=get_menu(),
        parse_mode="MarkDownV2",
    )
