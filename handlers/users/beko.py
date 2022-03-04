from aiogram import types
from keyboards.default.bekor import nastroyy
from loader import dp


# Echo bot
@dp.message_handler(text = 'ЧУВСТВИТЕЛЬНОСТЬ 🌿')
async def bot_echo(message: types.Message):
    await message.answer(text='🔫',reply_markup=nastroyy)

