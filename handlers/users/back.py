from aiogram import types
from keyboards.default.tasdiqlash import asosiy
from keyboards.default.telefon import telefon
from keyboards.default.bekor import nastroyy
from loader import dp


# Echo bot
@dp.message_handler(text='🔙Back')
async def bot_echo(message: types.Message):
    await message.answer(text='🔙Back',reply_markup=asosiy)

# Echo bot
@dp.message_handler(text='🔙Go')
async def bot_echo(message: types.Message):
    await message.answer(text='🔙Back',reply_markup=telefon)

# Echo bot
@dp.message_handler(text='🔚')
async def bot_echo(message: types.Message):
    await message.answer(text='🔚',reply_markup=nastroyy)