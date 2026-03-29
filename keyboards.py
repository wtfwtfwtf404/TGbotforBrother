from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Кто мы", callback_data="who_we_are"),
        InlineKeyboardButton("Модерация", callback_data="moderation"),
        InlineKeyboardButton("Купить курс", callback_data="buy_course")
    )

def payment_menu():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton("Оплатить", callback_data="pay"),
        InlineKeyboardButton("Назад", callback_data="cancel")
    )