from aiogram import types
from keyboards.default.realme import realme
from loader import dp


# Echo bot
@dp.message_handler(text='Realme🎯')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇷 ⚙',reply_markup=realme)

# Echo bot
@dp.message_handler(text='Realme C3')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 C3:\n\nобзор = 100\nКол=100\n2Х =100\n4Х =100\n8X =15\nDPI = 490')

# Echo bot
@dp.message_handler(text='Realme 7/7Pro')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 7/7 Pro:\n\nОбзор =100\nКалиматор = 98\n2x =100\n4x = 100\n8x =67\nDPI = 487')

# Echo bot
@dp.message_handler(text='Realme 6/6Pro')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 6/6:\n\nОбзор =100\nКалиматор = 100\n2x =100\n4x = 100\n8x =67\nDPI = 560')

# Echo bot
@dp.message_handler(text='Realme C12')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 C12:\n\nОбзор =100\nКол=100\n2Х =100\n4Х =100\n8X =15\nDPI = 619')

# Echo bot
@dp.message_handler(text='Realme 5i')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 5i:\n\nОбзор = 99\nКол=100\n2Х =100\n4Х =100\n8X =15\nDPI = 589')

# Echo bot
@dp.message_handler(text='Realme 5')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 5:\n\nОбзор=100\nКол=100\n2Х =100\n4Х =100\n8X =15\nDPI = 597')

# Echo bot
@dp.message_handler(text='Realme c11')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🎯 c11:\n\nОбзор=86\nКол=79\n2Х =100\n4Х =95\n8X =15\nDPI = 800')