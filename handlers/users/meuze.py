from aiogram import types
from keyboards.default.meuze import meuz
from loader import dp


# Echo bot
@dp.message_handler(text='Meizu🌪')
async def bot_echo(message: types.Message):
    await message.answer(text='Meizu🌪',reply_markup=meuz)

# Echo bot
@dp.message_handler(text='M3')
async def bot_echo(message: types.Message):
    await message.answer(text='Meizu🌪 M3:\n\nОбзор = 46\nКоллиматор = 70\n2x Прицел = 60\n4x Прицел = 55\n8x Прицел = 45')

# Echo bot
@dp.message_handler(text='M6')
async def bot_echo(message: types.Message):
    await message.answer(text='Meizu🌪 M6:\n\nОбзор = 100\nКоллиматор = 100\n2x Прицел = 80\n4x Прицел = 70\n8x Прицел = 50')