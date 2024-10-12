from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


def pagination_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="<-", callback_data="prev_day"),
        InlineKeyboardButton(text="->", callback_data="next_day"),
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back"),
    )
    return builder.as_markup()
