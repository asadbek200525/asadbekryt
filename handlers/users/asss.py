from aiogram import types
from keyboards.default.botyasash import botyashaw
from loader import dp


# Echo bot
@dp.message_handler(text='Bot yasatirish uchun zakas berish')
async def bot_echo(message: types.Message):
    await message.answer(text='Bot yasatirish uchun zakas berish',reply_markup=botyashaw)
