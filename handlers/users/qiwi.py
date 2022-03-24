from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.telnomer import russpasport
from keyboards.inline.psport import nomer

from loader import dp


# Echo bot
@dp.message_handler(text='Qiwi indinfikatsiya📣')
async def bot_echo(message: types.Message):
    await message.answer(text='Qiwi idinfikatsiya qilish uchun tanlang', reply_markup=russpasport)

from aiogram import types
from keyboards.default.telnomer import russpasport

from loader import dp


# Echo bot
@dp.message_handler(text='Russ pasport olish')
async def bot_echo(message: types.Message):
    await message.answer_photo(photo='https://t.me/sinov12345987/147',caption='Id boyicha raqamlarni tanlang' ,reply_markup=nomer)

@dp.callback_query_handler(text='1')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/148')

