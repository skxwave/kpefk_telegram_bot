from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards import get_admin_menu
from bot.misc.states import CreateUserState
from core import db_helper
from bot.middlewares import IsAdminMiddleware

router = Router()

router.message.middleware(IsAdminMiddleware())


@router.callback_query(F.data == "add_schedule")
async def add_schedule(callback: CallbackQuery):
    pass
