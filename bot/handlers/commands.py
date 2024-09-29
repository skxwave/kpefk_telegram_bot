from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.keyboards import get_menu

router = Router()


@router.message(Command("start", "menu"))
async def start_message(message: Message):
    await message.answer(
        "*Menu:*",
        reply_markup=get_menu(),
        parse_mode="MarkDownV2",
    )
