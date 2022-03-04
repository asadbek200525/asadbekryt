from aiogram import types
from keyboards.default.oppo import oppo
from loader import dp


# Echo bot
@dp.message_handler(text = 'Oppo🌀')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀',reply_markup=oppo)

# Echo bot
@dp.message_handler(text = 'As3')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 As3:\n\nобзор = 65 \nКоллиматор = 49 \n2x = 35 \n4x = 75 \n8x = 16')

# Echo bot
@dp.message_handler(text = 'A5 2020')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 A5 2020:\n\nnобзор = 100\nКол=100\n2Х =100\n4Х =100\n8X =15\nКнопка огня 83\nDpi=550')

# Echo bot
@dp.message_handler(text = 'A1')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 A1:\n\nобзор = 58 \nКоллиматор = 70\n2x = 80 \n4x = 89\n8x = 658x = 65')

# Echo bot
@dp.message_handler(text = '71k')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 71k:\n\nобзор=52\nКоллиматор=63\n2x=60\n4x=70\n8x=0')

# Echo bot
@dp.message_handler(text = 'A83')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 A83:\n\nобзор =100 \nКоллиматор = 100\n2x = 100\n4x = 80 \n8x = 50')

# Echo bot
@dp.message_handler(text = 'A72')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 A72:\n\nОбзор =100\nКалиматор = 98\n2x =100\n4x = 100\n8x =67\nDPI = 648\nKnopka = 60')

# Echo bot
@dp.message_handler(text = 'A53')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🌀 A53:\n\nОбзор =100\nКалиматор = 98\n2x =100\n4x = 100\n8x =67\nDPI = 623\nKnopka = 62')
