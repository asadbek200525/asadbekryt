from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy_tugma = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text='Tasdiqlash'),
           KeyboardButton(text='Bekor qilish')
       ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy_tugmaa = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text='Подтвердить'),
           KeyboardButton(text='Отмена')
       ]
    ],
    resize_keyboard=True
)