from aiogram import types
from keyboards.default.tasdiqlash import asosiy
from loader import dp


# Echo bot
@dp.message_handler(text='Glavniy menyu')
async def bot_echo(message: types.Message):
    await message.answer(text='🔙Glavniy menyu',reply_markup=asosiy)
