from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Schedule", callback_data="show_schedule"),
        InlineKeyboardButton(text="Group", callback_data="choose_group"),
    )
    return builder.as_markup()
