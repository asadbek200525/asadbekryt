from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(text='ochirish')
async def bot_echo(message: CallbackQuery):
    await message.message.delete()
