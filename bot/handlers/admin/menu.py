from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards import get_admin_menu
from bot.misc.states import CreateUserState
from core import db_helper
from bot.middlewares import IsAdminMiddleware

router = Router()

router.message.middleware(IsAdminMiddleware())


@router.message(Command("admin"))
async def admin_panel(message: Message):
    await message.answer(
        "*Admin panel:*",
        parse_mode="MarkDownV2",
        reply_markup=get_admin_menu(),
    )
