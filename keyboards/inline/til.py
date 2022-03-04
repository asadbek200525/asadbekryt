from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uzb 🇺🇿',callback_data='Uzb'),
            InlineKeyboardButton(text='Russ  🇷🇺',callback_data='rus')
        ]
    ]
)