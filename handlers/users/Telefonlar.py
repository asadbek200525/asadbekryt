from aiogram import types
from keyboards.default.bekor import nastroy
from loader import dp


# Echo bot
@dp.message_handler(text = 'Nastoyka Telefon📱')
async def bot_echo(message: types.Message):
    await message.answer(text='🔫',reply_markup=nastroy)
