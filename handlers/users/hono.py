from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='honor 3')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 3\n\nобзор=55\nКол=70\n2x=70\n4x=60\n8x=10')

# Echo bot
@dp.message_handler(text='honor 7')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 7\n\nобзор=60\nКол=57\n2x=57\n4x=51\n8x=30')

# Echo bot
@dp.message_handler(text='honor 7a')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 7a\n\nобзор=60\nКол=57\n2x=57\n4x=51\n8x=30')

# Echo bot
@dp.message_handler(text='honor 7x')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 7x\n\nобзор=91\nКол=72\n2x=61\n4x=59\n8x=21\nknopka=80\nDPI=700')

# Echo bot
@dp.message_handler(text='honor 8s')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 8s\n\nобзор=85\nКол=90\n2x=90\n4x=78\n8x=28\nknopka=80\nDPI=421')

# Echo bot
@dp.message_handler(text='honor 8a')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 8a\n\nобзор=95\nКол=100\n2x=100\n4x=100\n8x=77\nknopka=100\nDPI=500')

# Echo bot
@dp.message_handler(text='honor 8x')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 8x\n\nобзор=95\nКол=90\n2x=100\n4x=80\n8x=33\nknopka=60\nDPI=421')

# Echo bot
@dp.message_handler(text='honor 9a')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 9a\n\nобзор=99\nКол=85\n2x=86\n4x=73\n8x=100')

# Echo bot
@dp.message_handler(text='honor 9c')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 9c\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=50\nDPI=480')

# Echo bot
@dp.message_handler(text='honor 9 Lite')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 9 Lite\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=20\nDPI=480')

# Echo bot
@dp.message_handler(text='hono 10 Lite')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 10 Lite\n\nобзор=82\nКол=80\n2x=72\n4x=62\n8x=52\nDPI=421')

# Echo bot
@dp.message_handler(text='honor 20')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 20\n\nобзор=100\nКол=100\n2x=100\n4x=100\n8x=100\nknopka=80\nDPI=450')

# Echo bot
@dp.message_handler(text='honor 20 Pro')
async def bot_echo(message: types.Message):
    await message.answer(text='honor 20 Pro\n\nобзор=82\nКол=42\n2x=19\n4x=52\n8x=34')