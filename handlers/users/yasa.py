from aiogram import types
from keyboards.inline.bot import bot
from loader import dp


# Echo bot
@dp.message_handler(text='Nima uchun Telegram botlari biznes uchun muhim?')
async def bot_echo(message: types.Message):
    await message.answer(text='24/7 xizmat korsating\nMijozlar bilan samarali muloqot\nOrnatish va avtorizatsiyani talab qilmaydi.\nHar bir mijozga shaxsiy etibor.\nBotdagi puxta ishlab chiqilgan savollar yordamida siz xaridorni birinchi aloqadan to buyurtma berishgacha yetaklashingiz mumkin.\nMoslashuvchanlik va javob tezligi..')

from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='Chatbot qanday funktsiyalarni bajarishi mumkin?')
async def bot_echo(message: types.Message):
    await message.answer(text="Telegram’ning ko‘plab foydalanuvchilari botlar yordamida nafaqat o‘zingiz, balki biznesingiz uchun ham hayotni osonlashtirishingiz mumkinligini anglab ham etmaydi. Va eng muhimi, bunday imkoniyatlar va ma'lumotlarga ega bo'lgan biznes ushbu texnologiyalarni joriy qilmaganlarga nisbatan raqobatdosh ustunlikka ega.")