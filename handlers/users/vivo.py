from aiogram import types
from keyboards.default.vivo import vivo
from loader import dp


# Echo bot
@dp.message_handler(text='Vivo☄')
async def bot_echo(message: types.Message):
    await message.answer(text='Vivo☄',reply_markup=vivo)

# Echo bot
@dp.message_handler(text='Y96/LITE')
async def bot_echo(message: types.Message):
    await message.answer(text='Vivo☄ Y96/LITE:\n\nОбзор = 97 \nКоллиматор = 93\n2Х = 82 \n4Х = 81 \n8X = 0')

# Echo bot
@dp.message_handler(text='Y19')
async def bot_echo(message: types.Message):
    await message.answer(text='Vivo☄ Y19:\n\nОбзор 100\nКол 100\n2х 100\n4х 100\n8х 100\n')

# Echo bot
@dp.message_handler(text='Y11')
async def bot_echo(message: types.Message):
    await message.answer(text='Vivo☄ Y11:\n\nВсë на 100\nDPI = 500')