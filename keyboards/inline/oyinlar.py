from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

oyin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Free Fire',callback_data='free'),
            InlineKeyboardButton(text='Pubg',callback_data='pubg')
        ]
    ]
)