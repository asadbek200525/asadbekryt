from aiogram.types import CallbackQuery

from loader import dp


# Echo bot
@dp.callback_query_handler(text='KAFE')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="KAFELAR UCHUN BOT:\n\n-Kafelar uchun telegram bot. Bu sizga qanday yordam bera oladi?\n-Bu sizga sizning kafe yoki restaraningizdagi ho'randalaga alohida etibor va kechikmastan menyuni ko'rsatish va onlayn zakas berishni taminglaydi!\n-Bu yana afitsantlarga ehdiyojni kamaytiradi.")

# Echo bot
@dp.callback_query_handler(text='INTERNET')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="INTERNET MAGAZIN BOT:\n\n-Internet magazin telegram bot.Bu sizga qanday yordam bera oladi?\n-Szning tavarlaringizni tezroq sotish va sizning tavlaringiz bilan birma bir tanishtirib chiqishni taminlaydi!\nShuningdek tavarlaringiz ham tezroq sotilishiga yordam beradi.")

# Echo bot
@dp.callback_query_handler(text='DOSTAVKA')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="Yetkazib berish hizmati BOT:\n\n-Yetkazib berish hizmati uchun bot.Bu sizga qanday yordam beradi?\n-Bu sizga onlayn rejimda 24/7 hizmat ko'rsatishingiz mumkun va siz xaridorni birinchi aloqadan to buyurtma berishgacha yetaklashingiz mumkin.")

# Echo bot
@dp.callback_query_handler(text='OQUV')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="O'quv markazlari BOT:\n\nBu sizga qanday yordam bera oladi?\n-Sizning oquv markazingiz onlayn rejimda kurslarga yozilishni va kurslar bilan tanishib chiqishni taminlay oladi\n-Oquv kurslarini qanday sharoitda oqishini ko'rsatib bera oladi\n-Bunday botlar 24 hizmat ko'rsatadi")

# Echo bot
@dp.callback_query_handler(text='CHAT')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="Chat bot:\n\nBu sizga qanday yordam bera oladi?\n-Bunday botlar kop funksiyali bo'lib bu sizga har qanday kanallar gruppalar bilan ishlay oladigan bot bo'ladi.")

# Echo bot
@dp.callback_query_handler(text='c')
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="API BOT:\n\nBu sizga qanday yordam bera oladi?\n-Bunday botlar har qanday web saytlar bilan ishlay olishni taminlaydi")