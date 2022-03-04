from aiogram import types
from keyboards.inline.botyasash import boyyasash
from loader import dp


# Echo bot
@dp.message_handler(text='Telegram bot turlari')
async def bot_echo(message: types.Message):
    await message.answer(text='-Telegram bot turlari.\n-Ularning nima uchun kerakligi?\n-Telegram botlar nima vazifa qilishi.\n-Biz sizga qanday botlar yasab bera olamiz👇🏻',reply_markup=boyyasash)