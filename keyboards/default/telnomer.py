from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

russpasport = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text='Qiwi indinfikatsiya 0 dan organish'),
       ],
        [
            KeyboardButton(text='Russ pasport olish')
        ],
        [
            KeyboardButton(text='glavniy menyu')
        ]
    ],
    resize_keyboard=True
)
