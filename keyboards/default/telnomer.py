from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

nomer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon',request_contact=True),
            KeyboardButton(text='Bekor qilish')
        ]
    ]
)