from datetime import datetime, timedelta

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

from core import db_helper
from bot.keyboards import pagination_keyboard
from bot.handlers.commands import send_menu

router = Router()

current_date = datetime.now().date()


async def schedule_output(telegram_id, day):
    user = await db_helper.find_user(telegram_id)
    lessons = await db_helper.find_lessons(user.group, day=day)
    text = f"*Weekday*: {day}\n\n"
    for lesson in lessons:
        text += (
            f"*Lesson number*: {lesson.lesson_number}\n"
            f"*Subject*: {lesson.subject}\n"
            f"*Classroom*: {lesson.classroom}\n"
            f"*Teacher*: {lesson.teacher}\n\n"
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
    await send_menu(callback.message)
