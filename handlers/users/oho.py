from aiogram import types
from keyboards.default.Redmi import redmi
from loader import dp


# Echo bot
@dp.message_handler(text='Redmiâ')
async def bot_echo(message: types.Message):
    await message.answer(text='ð¹ ð´ ðµ  ð³ ð¦ ð¸ ð¹ ð· ð´ ð¾ ð° ð¦  ð· ðª ð© ð² ð® â',reply_markup=redmi)
