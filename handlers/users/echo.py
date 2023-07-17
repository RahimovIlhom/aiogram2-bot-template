from aiogram import types

from filters import PrivateFilter
from loader import dp


# Echo bot
@dp.message_handler(PrivateFilter(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
