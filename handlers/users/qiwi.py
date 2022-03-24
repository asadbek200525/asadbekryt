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

@dp.callback_query_handler(text='2')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/149')

@dp.callback_query_handler(text='3')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/151')

@dp.callback_query_handler(text='4')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/152')

@dp.callback_query_handler(text='5')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/153')

@dp.callback_query_handler(text='6')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/154')

@dp.callback_query_handler(text='7')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/155')

@dp.callback_query_handler(text='8')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/156')

@dp.callback_query_handler(text='9')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/157')

@dp.callback_query_handler(text='10')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/158')
