from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram import F

from core import db_helper
from bot.keyboards import get_menu

router = Router()


@router.callback_query(F.data == "show_schedule")
async def get_schedule(callback: CallbackQuery):
    user = await db_helper.find_user(callback.from_user.id)
    lessons = await db_helper.find_lessons(user.group, day="Tuesday")
    for lesson in lessons:
        text = (
            f"*Day*: {lesson.day}\n"
            f"*Lesson number*: {lesson.lesson_number}\n"
            f"*Subject*: {lesson.subject}\n"
            f"*Classroom*: {lesson.classroom}\n"
            f"*Teacher*: {lesson.teacher}\n"
        )
        await callback.message.answer(text=text, parse_mode="MarkDownV2")
