from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uzb πΊπΏ',callback_data='Uzb'),
            InlineKeyboardButton(text='Russ  π·πΊ',callback_data='rus')
        ]
    ]
)