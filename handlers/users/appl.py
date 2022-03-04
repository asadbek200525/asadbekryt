from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='5s')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone 5s nastroyka\nобзор=87\nКоллиматор=60\n2x=60\n4x=55\n8x=15')



# Echo bot
@dp.message_handler(text='6')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone 6 nastroyka\nОбзор=98\nКол=100\n2x=100\n4x=100\n8x=0\nKnopka=63\nDPI=114')

# Echo bot
@dp.message_handler(text='11')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone 11 nastroyka\nОбзор=100\nКол=100\n2x=100\n4x=100\n8x=40\nKnopka=93')

# Echo bot
@dp.message_handler(text='7')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone 7 nastroyka\nОбзор=86\nКол=98\n2x=100\n4x=94\n8x=44')


# Echo bot
@dp.message_handler(text='SE')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone SE nastroyka\nОбзор=89\nКол=73\n2x=53\n4x=77\n8x=0')

# Echo bot
@dp.message_handler(text='XR')
async def bot_echo(message: types.Message):
    await message.answer(text='Iphone XR nastroyka\nОбзор=100\nКол=80\n2x=80\n4x=70\n8x=0')





