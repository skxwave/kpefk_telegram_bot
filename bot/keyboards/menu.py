from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Розклад", callback_data="show_schedule"),
        InlineKeyboardButton(text="Змінити групу", callback_data="choose_group"),
        InlineKeyboardButton(text="Інформація", callback_data="group_info"),
        InlineKeyboardButton(text="Вийти", callback_data="exit"),
    )
    builder.adjust(2)
    return builder.as_markup()


def get_admin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Add schedule", callback_data="add_schedule"),
        InlineKeyboardButton(text="Delete schedule", callback_data="delete_schedule"),
    )
    builder.row(
        InlineKeyboardButton(text="Delete all", callback_data="delete_all"),
    )
    return builder.as_markup()
