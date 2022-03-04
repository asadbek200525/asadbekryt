from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.til import til

from loader import dp,db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.full_name
    fam = message.from_user.last_name
    username = message.from_user.username
    tgid = message.from_user.id
    try:
        db.user_qoshish(ism=ism,fam=fam,username=username,tg_id=tgid)
    except Exception as xatolik :
        print(xatolik)
    await message.answer(f"Salom, {message.from_user.full_name} Tilni tanglang 🇺🇿 : Привет {message.from_user.full_name} Виберите язик 🇷🇺",reply_markup=til)

 #Free Fire botimizga hush kelibsiz \n \n Добро пожаловать в наш бот Free Fire