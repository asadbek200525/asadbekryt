from aiogram import types
from keyboards.default.Redmi import redmi
from loader import dp


# Echo bot
@dp.message_handler(text='Redmi❄')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇷 🇪 🇩 🇲 🇮 ⚙',reply_markup=redmi)
