from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.inline.psport import nomerr,nomer
from keyboards.inline.oyinlar import oyin

from loader import dp

@dp.callback_query_handler(text='ochirish')
async def bot_echo(message: CallbackQuery):
    await message.message.delete()

@dp.callback_query_handler(text='00')
async def bot_echo(message: CallbackQuery):
    await message.message.delete()
    await message.message.answer_photo(photo='https://t.me/sinov12345987/150',caption='Id boyicha raqamlarni tanlang',reply_markup=nomerr)

@dp.callback_query_handler(text='0')
async def bot_echo(message: CallbackQuery):
    await message.message.delete()
    await message.message.answer_photo(photo='https://t.me/sinov12345987/147',caption='Id boyicha raqamlarni tanlang',reply_markup=nomer)

