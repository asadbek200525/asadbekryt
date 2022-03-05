from aiogram import types
from keyboards.inline.bot import bot
from loader import dp


# Echo bot
@dp.message_handler(text = 'Bot uchun zakas')
async def bot_echo(message: types.Message):
    await message.answer(text='Bot yasab berish hizmati uchun pastadagi adminga yozing🏻',reply_markup=bot)
