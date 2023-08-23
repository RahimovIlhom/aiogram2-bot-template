from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Send contact", request_contact=True)],
    ],
    resize_keyboard=True
)
