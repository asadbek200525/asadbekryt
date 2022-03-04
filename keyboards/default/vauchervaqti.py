from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

vaqti = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 haftalik'),
            KeyboardButton(text='1 oylik')
        ],
        [
            KeyboardButton(text='Bekor qilish')
        ]
    ],
    resize_keyboard=True
)


from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

vaqtii = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 неделя'),
            KeyboardButton(text='1 месяц')
        ],
        [
            KeyboardButton(text='🔙Отменит')
        ]
    ],
    resize_keyboard=True
)