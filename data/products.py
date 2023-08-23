from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product

ds_praktikum = Product(
    title="Data Science va Sun'iy intellekt",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Praktikum',
            amount=15000,  # 150.00$
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-1000,  # -10.00$
        ),
    ],
    start_parameter="create_invoice_ds_praktikum",
    photo_url='https://files.glotr.uz/company/000/025/421/products/2021/07/12/2021-07-12-10-24-35-183912-95803e7db7edc54aac832818f69ef30a.jpg?_=ozbol',
    photo_width=1200,
    photo_height=703,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=500,  # 5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,  # 1.00$
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://rukminim2.flixcart.com/image/850/1000/kq8dua80/book/v/f/2/zero-to-mastery-in-python-programming-best-python-book-for-original-imag4ab2gzadhskq.jpeg?q=90',
    photo_width=757,
    photo_height=1000,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,  # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100),
        LabeledPrice(
            '3 ish kunida yetkazish', 100),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 100),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100)
                                       ])
