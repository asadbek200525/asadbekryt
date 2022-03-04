from aiogram import types
from keyboards.default.honor import honor
from loader import dp


# Echo bot
@dp.message_handler(text='Honor🎮')
async def bot_echo(message: types.Message):
    await message.answer(text='🇹 🇴 🇵  🇳 🇦 🇸 🇹 🇷 🇴 🇾 🇰 🇦  🇭 🇴 🇳 🇴 🇷 ⚙',reply_markup=honor)
