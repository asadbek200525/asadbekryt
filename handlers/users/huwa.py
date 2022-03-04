from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='P20')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 P20 \n\nобзор = 90\nКол=100\n2x=85\n4x=75\n8x=0')

# Echo bot
@dp.message_handler(text='Y5 2017')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 Y5 2017\n\nобзор=85\nКол=60\n2x=80\n4x=80\n8x=80')

# Echo bot
@dp.message_handler(text='Y5 2019')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 Y5 2019\n\nобзор=100\nКол=96\n2x=100\n4x=100\n8x=85\nknopka=63\nDPI=600')

# Echo bot
@dp.message_handler(text='Y6 2019')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 Y6 2019\n\nобзор=98\nКол=100\n2x=100\n4x=90\n8x=0\nknopka=90')

# Echo bot
@dp.message_handler(text='P smart')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 P smart\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=50\nknopka=56\nDPI=423')

# Echo bot
@dp.message_handler(text='P smart 2019')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 P smart 2019\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=50\nDPI=741')

# Echo bot
@dp.message_handler(text='P 20 pro')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 P 20 pro\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=75\nknopka=45\nDPI=550')

# Echo bot
@dp.message_handler(text='Y 7 2019')
async def bot_echo(message: types.Message):
    await message.answer(text='Huwawe💧 Y 7 2019\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=100\nknopka=41\nDPI=500')