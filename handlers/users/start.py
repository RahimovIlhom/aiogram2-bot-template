from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType

from keyboards.default import menu_button_markup, phone_button_markup
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    user = db.select_user(message.from_user.id)
    if user:
        await message.answer(f"Mahsulot sotib olish uchun menu tugmasini bosing!",
                             reply_markup=menu_button_markup)
        return
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Botdan foydalanish uchun kontaktingizni yuboring!",
                         reply_markup=phone_button_markup)
    await state.set_state('phone_number')


@dp.message_handler(state='phone_number', content_types="contact", is_sender_contact=True)
async def phone_send(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    phone_number = message.contact.phone_number
    mention = message.from_user.get_mention()
    db.add_user(user_id, full_name, phone_number, mention)
    await message.answer(f"Mahsulot sotib olish uchun menu tugmasini bosing!",
                         reply_markup=menu_button_markup)
    await state.finish()


@dp.message_handler(state='phone_number', content_types=ContentType.ANY)
async def err_phone_send(message: types.Message, state: FSMContext):
    await message.answer(f"Botdan foydalanish uchun kontaktingizni yuboring!",
                         reply_markup=phone_button_markup)
