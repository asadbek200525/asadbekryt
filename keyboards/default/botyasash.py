from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

botyashaw = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Nima uchun Telegram botlari biznes uchun muhim?')
        ],
        [
            KeyboardButton(text='Chatbot qanday funktsiyalarni bajarishi mumkin?')
        ],
        [
            KeyboardButton(text='Telegram bot turlari')
        ],
        [
            KeyboardButton(text='Bot uchun zakas')
        ],
        [
            KeyboardButton(text='Glavniy menyu')
        ]
    ],
    resize_keyboard=True
)