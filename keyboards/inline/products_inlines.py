from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


from loader import db

menu_cd = CallbackData('show_menu', 'level', 'category_id', 'item_id')
buy_item = CallbackData('buy', 'item_id')


def make_callback_data(level, category_id=0, item_id=0):
    return menu_cd.new(
        level=level, category_id=category_id, item_id=item_id
    )


async def category_keyboard():
    # eng quyi qavat (0-qavat)
    CURRENT_LEVEL = 0

    category_markup = InlineKeyboardMarkup(row_width=1)

    # categories
    categories = db.select_categories()

    # categorylarni for yordamida aylanish
    for category in categories:

        # callback_data yasash
        callback = make_callback_data(level=CURRENT_LEVEL+1, category_id=category[0])

        # inline button yasash
        inline_button = InlineKeyboardButton(text=category[1], callback_data=callback)
        category_markup.insert(inline_button)

    # inline keyboardlarni qaytarish
    return category_markup


async def items_keyboard(category_id):
    # 1 - qavat
    CURRENT_LEVEL = 1

    products_markup = InlineKeyboardMarkup(row_width=1)

    # products in category
    products = db.select_category_products(category_id=category_id)

    # productlarni for yordamida aylanish
    for product in products:
        # callback_data yasash
        callback = make_callback_data(level=CURRENT_LEVEL + 1, category_id=product[4], item_id=product[0])

        # inline button yasash
        inline_button = InlineKeyboardButton(text=product[1], callback_data=callback)
        products_markup.insert(inline_button)

    # Orqaga tugamsini qo'shish
    products_markup.row(
        InlineKeyboardButton(
            text="Orqaga", callback_data=make_callback_data(level=CURRENT_LEVEL-1)
        )
    )

    # inline keyboardlarni qaytarish
    return products_markup


async def item_keyboard(item_id):
    # 2 - qavat
    CURRENT_LEVEL = 2

    product_markup = InlineKeyboardMarkup(row_width=1)
    product_markup.row(
        InlineKeyboardButton(
            text=f"🛒 Xarid qilish", callback_data=buy_item.new(item_id=item_id)
        )
    )
    product_markup.row(
        InlineKeyboardButton(
            text="❌",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL + 1
            ),
        )
    )
    return product_markup
