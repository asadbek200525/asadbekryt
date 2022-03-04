from aiogram import types
from keyboards.default.telefon import telefon
from loader import dp


# Echo bot
@dp.message_handler(text = '🔙Go back')
async def bot_echo(message: types.Message):
    await message.answer(text='🌐',reply_markup=telefon)