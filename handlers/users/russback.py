from aiogram import types
from keyboards.default.tasdiqlash import russ
from loader import dp


# Echo bot
@dp.message_handler(text = '🔙Bacck')
async def bot_echo(message: types.Message):
    await message.answer(text='🔫',reply_markup=russ)

