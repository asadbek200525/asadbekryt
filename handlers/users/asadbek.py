from aiogram import types
from keyboards.inline.bot import bot
from loader import dp


# Echo bot
@dp.message_handler(text='Bot uchun zakas')
async def bot_echo(message: types.Message):
    await message.answer(text="Bot uchun zakas berish uchun pastagi tugmani bosing👇🏻",reply_markup=bot)
