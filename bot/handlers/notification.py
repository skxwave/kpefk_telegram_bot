from datetime import datetime, timedelta
import requests

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

from core import db_helper
from bot.keyboards import get_back_button
from bot.handlers.commands import send_menu

router = Router()


@router.callback_query(F.data == "group_info")
async def get_group_info(callback: CallbackQuery):
    user = await db_helper.find_user(callback.from_user.id)
    group = user.group
    info = requests.get(
        f"https://skxwave.pythonanywhere.com/api/v1/groups/info/{group}"
    ).json()
    text = "*Інформація*\n\n"
    for item in info["result"]:
        text += f"{item['message']}"
    await callback.message.edit_text(
        text=text,
        parse_mode="MarkDownV2",
        reply_markup=get_back_button(),
    )


# @router.callback_query(F.data == "back_menu")
# async def back(callback: CallbackQuery):
#     await send_menu(callback.message, callback.from_user.id)
