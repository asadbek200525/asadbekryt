from aiogram import types
from keyboards.default.iphone import iphone
from keyboards.default.Redmi import redmii
from keyboards.default.huawe import huawee
from keyboards.default.honor import honorr
from keyboards.default.oppo import oppoo
from keyboards.default.samsung import samsungg
from keyboards.default.meuze import meuzz
from keyboards.default.lg import lgg
from keyboards.default.realme import realmee
from keyboards.default.vivo import vivoo
from keyboards.default.htc import htc,htcc
from loader import dp


# Echo bot
@dp.message_handler(text='Iphone🔥')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇮 🇵 🇭 🇴 🇳 🇪 ⚙',reply_markup=iphone)

from aiogram import types
from keyboards.default.iphone import iphonee
from loader import dp


# Echo bot
@dp.message_handler(text='АЙФОН🐬')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇮 🇵 🇭 🇴 🇳 🇪 ⚙',reply_markup=iphonee)

# Echo bot
@dp.message_handler(text='XIAOMI🐳')
async def bot_echo(message: types.Message):
    await message.answer(text='XIAOMI🐳',reply_markup=redmii)

# Echo bot
@dp.message_handler(text='HUAWEI🦄')
async def bot_echo(message: types.Message):
    await message.answer(text='HUAWEI🦄',reply_markup=huawee)

# Echo bot
@dp.message_handler(text='Honor🐼')
async def bot_echo(message: types.Message):
    await message.answer(text='Honor🐼',reply_markup=honorr)

# Echo bot
@dp.message_handler(text='Oppo🐿️')
async def bot_echo(message: types.Message):
    await message.answer(text='Oppo🐿️',reply_markup=oppoo)

# Echo bot
@dp.message_handler(text='Samsung🦊')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung🦊',reply_markup=samsungg)

# Echo bot
@dp.message_handler(text='Meizu 🐰')
async def bot_echo(message: types.Message):
    await message.answer(text='Meizu 🐰',reply_markup=meuzz)

# Echo bot
@dp.message_handler(text='LG🐴')
async def bot_echo(message: types.Message):
    await message.answer(text='LG🐴',reply_markup=lgg)

# Echo bot
@dp.message_handler(text='Realme🐻')
async def bot_echo(message: types.Message):
    await message.answer(text='Realme🐻',reply_markup=realmee)


# Echo bot
@dp.message_handler(text='Vivo🐈')
async def bot_echo(message: types.Message):
    await message.answer(text='Vivo🐈',reply_markup=vivoo)

# Echo bot
@dp.message_handler(text='HTC🌡')
async def bot_echo(message: types.Message):
    await message.answer(text='HTC🌡',reply_markup=htc)

# Echo bot
@dp.message_handler(text='htc one m8')
async def bot_echo(message: types.Message):
    await message.answer(text='HTC🌡 htc one m8:\n\nВсе 100, дпи 551, кнопка 74')

# Echo bot
@dp.message_handler(text='HTC🐱')
async def bot_echo(message: types.Message):
    await message.answer(text='HTC🐱',reply_markup=htcc)