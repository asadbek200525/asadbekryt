from aiogram import types
from keyboards.default.hudd import hudd
from loader import dp


# Echo bot
@dp.message_handler(text = 'HUD🗿')
async def bot_echo(message: types.Message):
    await message.answer(text='Nastroyka yutuberov',reply_markup=hudd)
