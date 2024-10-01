from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.misc.states import SetGroupState
from bot.handlers.commands import send_menu
from core import db_helper

router = Router()


@router.callback_query(F.data == "choose_group")
async def set_group(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Enter your group:")
    await state.set_state(SetGroupState.group)


@router.message(SetGroupState.group)
async def store_group(message: Message, state: FSMContext):
    await db_helper.set_group(
        telegram_id=message.from_user.id,
        group=int(message.text),
    )
    await message.reply("Group added!")
    await send_menu(message)
    await state.clear()
