from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu categories")],
    ],
    resize_keyboard=True
)
