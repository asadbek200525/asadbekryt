
from aiogram.types import CallbackQuery

from keyboards.default.tasdiqlash import asosiy,russ
from loader import dp


# Echo bot
@dp.callback_query_handler(text='Uzb')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text='Free Fire botimizga hush kelibsiz 😊 ',reply_markup=asosiy)


# Echo bot
@dp.callback_query_handler(text='rus')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text='Добро пожаловать в наш бот Free Fire😊 ',reply_markup=russ)