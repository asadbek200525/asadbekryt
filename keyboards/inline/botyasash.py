from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

boyyasash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Kafe restoranlar',callback_data="KAFE"),
            InlineKeyboardButton(text='Internet magazin',callback_data="INTERNET")
        ],
        [
            InlineKeyboardButton(text='Yetkazib berish xizmati',callback_data="DOSTAVKA"),
            InlineKeyboardButton(text="O'quv markazlari",callback_data="OQUV")
        ],
        [
            InlineKeyboardButton(text="Chat bot",callback_data="CHAT"),
            InlineKeyboardButton(text="API",callback_data="c")

        ],

        ]
)