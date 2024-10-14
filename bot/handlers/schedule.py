from datetime import datetime, timedelta
import requests

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

from core import db_helper
from bot.keyboards import pagination_keyboard
from bot.handlers.commands import send_menu

router = Router()

current_date = datetime.now().date()


async def schedule_output(telegram_id, day):
    if day in ["Saturday", "Sunday"]:
        return f"*{day}*\n\n"

    user = await db_helper.find_user(telegram_id)
    lessons = requests.get(
        f"https://skxwave.pythonanywhere.com/api/v1/schedule/{user.group}"
    )

    is_numerator = requests.get(
        "https://skxwave.pythonanywhere.com/api/v1/schedule/info/"
    ).json()["result"]["is_numerator"]

    text = f"*День*: {day}\n\n"

    for lesson in lessons.json()["result"][day]:
        title = (
            lesson["title_denom"]
            if lesson["title_denom"] and not is_numerator
            else lesson["title"]
        )
        room = (
            lesson["room_denom"]
            if lesson["room_denom"] and not is_numerator
            else lesson["room"]
        )
        teacher = (
            lesson["teacher_denom"]
            if lesson["teacher_denom"] and not is_numerator
            else lesson["teacher"]
        )

        if title:
            text += (
                f"*Номер:* {lesson['number']}\n"
                f"*Предмет:* {title}\n"
                f"*Кабінет:* {room}\n"
                f"*Викладач:* {teacher}\n\n"
            )
    return text


async def send_schedule(callback: CallbackQuery):
    day = current_date.strftime("%A")
    text = await schedule_output(callback.from_user.id, day=day)

    await callback.message.edit_text(
        text=text,
        parse_mode="MarkDownV2",
        reply_markup=pagination_keyboard(),
    )


@router.callback_query(F.data == "show_schedule")
async def get_schedule(callback: CallbackQuery):
    global current_date
    current_date = datetime.now().date()
    await send_schedule(callback)


@router.callback_query(F.data == "prev_day")
async def paginate_schedule(callback: CallbackQuery):
    global current_date
    current_date -= timedelta(days=1)
    await send_schedule(callback)


@router.callback_query(F.data == "next_day")
async def paginate_schedule(callback: CallbackQuery):
    global current_date
    current_date += timedelta(days=1)
    await send_schedule(callback)


@router.callback_query(F.data == "back")
async def close_schedule(callback: CallbackQuery):
    await callback.message.delete()
    await send_menu(callback.message, callback.from_user.id)
