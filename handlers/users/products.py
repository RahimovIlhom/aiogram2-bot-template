from typing import Union

from aiogram.types import Message, CallbackQuery

from keyboards.inline import (
    menu_cd,
    buy_item,
    category_keyboard,
    items_keyboard,
    item_keyboard)
from loader import dp, db, bot


@dp.message_handler(text="Menu categories")
async def menu(msg: Message):
    await list_categories(msg)


async def list_categories(message: Union[Message, CallbackQuery], **kwargs):
    markup = await category_keyboard()

    if isinstance(message, Message):
        await message.answer("Kategoriyani tanlang:", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_items(call: CallbackQuery, category_id, **kwargs):
    markup = await items_keyboard(category_id)

    await call.message.edit_text("Mahsulotni tanlang: ", reply_markup=markup)


async def show_item(call: CallbackQuery, category_id, item_id, **kwargs):
    markup = await item_keyboard(item_id=item_id)

    product = db.select_product(product_id=item_id)

    photo_path = product[5]
    info = f"<b>Brand</b>\n{product[1]}\n\n" \
           f"<b>Izoh</b>\n{product[2]}\n\n" \
           f"<b>Narxi</b>: <tg-spoiler>${product[3]}</tg-spoiler>\n\n" \
           f"<i><b>Kategory: {db.select_category(product[4])[1]}</b></i>"
    if photo_path:
        with open(f'{photo_path}', 'rb') as photo:
            await bot.send_photo(call.message.chat.id, photo, info, reply_markup=markup)
    else:
        await call.message.answer(info, reply_markup=markup)


async def remove_item(call: CallbackQuery, **kwargs):
    await call.message.delete()


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    # qaysi qavatda ekanligni bilish
    current_level = callback_data.get('level')

    # qaysi category id da ekanligni bilish
    category_id = callback_data.get('category_id')

    # qaysi productni ko'rayotagnligini bilish
    item_id = callback_data.get('item_id')

    levels = {
        '0': list_categories,  # kategories list funksiyasini qaytaramiz!
        '1': list_items,  # products list funksiyasini qaytaramiz!
        '2': show_item,  # product show funksiyasini qaytaramiz!
        '3': remove_item,  # remove item funksiyasini qaytaramiz!
    }

    current_level_function = levels[current_level]

    await current_level_function(call, category_id=category_id, item_id=item_id)
