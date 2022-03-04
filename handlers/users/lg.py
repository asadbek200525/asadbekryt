from aiogram import types
from keyboards.default.lg import lg
from loader import dp


# Echo bot
@dp.message_handler(text='LG🧩')
async def bot_echo(message: types.Message):
    await message.answer(text='Meizu🌪',reply_markup=lg)

# Echo bot
@dp.message_handler(text='Q6A')
async def bot_echo(message: types.Message):
    await message.answer(text='LG 🧩 Q6A:\n\nобзор = 66\nКоллиматор = 79\n2x = 69 \n4x = 65\n8x = 27')