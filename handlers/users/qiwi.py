from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.telnomer import russpasport
from keyboards.inline.psport import nomer
from keyboards.inline.oyinlar import oyin

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
    await message.message.answer_document(document='https://t.me/sinov12345987/148',reply_markup=oyin)

@dp.callback_query_handler(text='2')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/149',reply_markup=oyin)

@dp.callback_query_handler(text='3')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/151',reply_markup=oyin)

@dp.callback_query_handler(text='4')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/152',reply_markup=oyin)

@dp.callback_query_handler(text='5')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/153',reply_markup=oyin)

@dp.callback_query_handler(text='6')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/154',reply_markup=oyin)

@dp.callback_query_handler(text='7')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/155',reply_markup=oyin)

@dp.callback_query_handler(text='8')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/156',reply_markup=oyin)

@dp.callback_query_handler(text='9')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/157',reply_markup=oyin)

@dp.callback_query_handler(text='10')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/158',reply_markup=oyin)

@dp.callback_query_handler(text='11')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/159',reply_markup=oyin)

@dp.callback_query_handler(text='12')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/160',reply_markup=oyin)

@dp.callback_query_handler(text='13')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/161',reply_markup=oyin)

@dp.callback_query_handler(text='14')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/162',reply_markup=oyin)

@dp.callback_query_handler(text='15')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/163',reply_markup=oyin)

@dp.callback_query_handler(text='16')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/164',reply_markup=oyin)

@dp.callback_query_handler(text='17')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/165',reply_markup=oyin)

@dp.callback_query_handler(text='18')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/166',reply_markup=oyin)

@dp.callback_query_handler(text='19')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/167',reply_markup=oyin)

@dp.callback_query_handler(text='20')
async def bot_echo(message: CallbackQuery):
    await message.message.answer_document(document='https://t.me/sinov12345987/168',reply_markup=oyin)