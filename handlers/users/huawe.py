from aiogram import types
from keyboards.default.huawe import huawe
from loader import dp


# Echo bot
@dp.message_handler(text='Huwaweð§')
async def bot_echo(message: types.Message):
    await message.answer(text='ð¹ ð´ ðµ  ð³ ð¦ ð¸ ð¹ ð· ð´ ð¾ ð° ð¦  ð­ ðº ð¦ ð¼ ðª â',reply_markup=huawe)
