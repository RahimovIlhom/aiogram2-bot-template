from aiogram import types

from aiogram.dispatcher.filters import BoundFilter


class PrivateFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
