from aiogram import types

from loader import dp,db,bot

from states.holatlar import Forma
# Echo bot
@dp.message_handler(commands='post',chat_id=1035757120)
async def bot_echo(message: types.Message):
    await message.answer(text='Postni yuborish uchun tashlan')
    await Forma.post_qabul_qilish.set()

@dp.message_handler(chat_id=1035757120,state=Forma.post_qabul_qilish)
async def bot_echo(message: types.Message):
    post = message.text

    userlar = db.select_all_foydalanuvchilar()
    await message.answer(text=f'{userlar}')


