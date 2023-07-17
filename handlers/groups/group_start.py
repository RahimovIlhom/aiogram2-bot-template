from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import AdminFilter, GroupFilter
from loader import dp


@dp.message_handler(GroupFilter(), AdminFilter(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} siz adminsiz va guruhdasiz!")


@dp.message_handler(GroupFilter(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} siz guruhdasiz!")
