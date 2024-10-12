import requests

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.misc.states import SetGroupState
from bot.handlers.commands import send_menu
from core import db_helper
from bot.misc.utils import group_exist

router = Router()


@router.callback_query(F.data == "choose_group")
async def set_group(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введіть номер своєї групи:")
    await state.set_state(SetGroupState.group)


@router.message(SetGroupState.group)
async def store_group(message: Message, state: FSMContext):
    if await group_exist(message.text):
        await db_helper.set_group(
            telegram_id=message.from_user.id,
            group=int(message.text),
        )
        await message.reply("Група додана!")
        await send_menu(message)
        await state.clear()
    else:
        await message.reply("Група не існує.")
