import requests

from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards import get_menu
from bot.misc.states import CreateUserState
from core import db_helper
from bot.misc.utils import group_exist

router = Router()


async def send_menu(message: Message):
    await message.answer(
        "*Меню:*",
        reply_markup=get_menu(),
        parse_mode="MarkDownV2",
    )


@router.message(Command("start", "menu"))
async def start_message(message: Message, state: FSMContext):
    user = await db_helper.find_user(int(message.from_user.id))
    if not user:
        await state.set_state(CreateUserState.group)
        await message.answer("Введіть номер своєї групи:")
        return
    await send_menu(message)


@router.message(CreateUserState.group)
async def create_user(message: Message, state: FSMContext):
    if await group_exist(message.text):
        await db_helper.create_user(
            username=message.from_user.username,
            telegram_id=message.from_user.id,
            group=int(message.text),
        )
        await message.answer("Вітаємо!")
        await send_menu(message)
        await state.clear()
    else:
        await message.reply("Група не існує.")
