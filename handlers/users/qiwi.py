from aiogram import types
from keyboards.default.telnomer import russpasport

from loader import dp


# Echo bot
@dp.message_handler(text='Qiwi indinfikatsiya📣')
async def bot_echo(message: types.Message):
    await message.answer(text='Qiwi idinfikatsiya qilish uchun tanlang', reply_markup=russpasport)
