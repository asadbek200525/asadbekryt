from aiogram import types
from keyboards.default.huawe import huawe
from loader import dp


# Echo bot
@dp.message_handler(text='Huwawe💧')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇭 🇺 🇦 🇼 🇪 ⚙',reply_markup=huawe)
