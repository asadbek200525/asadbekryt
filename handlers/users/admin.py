from aiogram import types
from aiogram.dispatcher import FSMContext

from states.admin import admin
from keyboards.default.almazlar import asosiy_tugma
from keyboards.default.tasdiqlash import asosiy
from loader import dp, bot

@dp.message_handler(text='ADMIN BILAN BOGLANISH')
async def bot_echo(message: types.Message):
    await message.answer(text="Nima uchun admin bilan bog'lanmoqchisz:\nQisqacha yozib qoldiring",reply_markup=bekor)
    await admin.nimauchunadminkerak.set()
@dp.message_handler(state=admin.nimauchunadminkerak,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=admin.nimauchunadminkerak)
async def bot_echo(message: types.Message,state: FSMContext):
    nimauchunadminkerak = message.text
    await state.update_data({'nimauchunadminkerak': nimauchunadminkerak})
    await message.answer(text='Telegram akauntingiz yoki nomeringizni qoldiring:\nadmining ozi siz bilan boglanadi', reply_markup=bekor)
    await admin.akaunt.set()
@dp.message_handler(state=admin.akaunt,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=admin.akaunt)
async def bot_echo(message: types.Message,state: FSMContext):
    akaunt = message.text
    await state.update_data({'akaunt': akaunt})

    data = await state.get_data()
    nimauchunadminkerak = data.get('nimauchunadminkerak')
    akaunt = data.get('akaunt')

    matn = f"ADMIN BILAN BOGLANISH: \n\n👤Nima uchun admin kerakligi:{nimauchunadminkerak}\n" \
           f"📅Akaunt vs tel: {akaunt}\n"\

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
    await admin.admingayuborish.set()

@dp.message_handler(state=admin.admingayuborish, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Yozgan habaringiz adminga yuborilmadi',reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=admin.admingayuborish, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida siz bilan boglanamiz')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    nimauchunadminkerak = data.get('nimauchunadminkerak')
    akaunt = data.get('akaunt')



    matn +=f'Nima uchun admin kerakligi: {nimauchunadminkerak}\n'\
           f'Akaunt yoki telefon nomer: {akaunt}\n'\

    await message.answer(text='.', reply_markup=asosiy)
    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=asosiy)
    await state.finish()


from aiogram import types
from aiogram.dispatcher import FSMContext

from states.admin import rusadmin
from keyboards.default.kunlari import bekor
from keyboards.default.almazlar import asosiy_tugmaa
from keyboards.default.tasdiqlash import russ
from loader import dp, bot

@dp.message_handler(text='ADMIN BILAN BOGLANISH')
async def bot_echo(message: types.Message):
    await message.answer(text="Nima uchun admin biulan bog'lanmoqchisz:\nQisqacha yozib qoldiring",reply_markup=bekor)
    await rusadmin.nimauchunadminkerak.set()
@dp.message_handler(state=rusadmin.nimauchunadminkerak,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=russ)
    await state.finish()
@dp.message_handler(state=rusadmin.nimauchunadminkerak)
async def bot_echo(message: types.Message,state: FSMContext):
    nimauchunadminkerak = message.text
    await state.update_data({'nimauchunadminkerak': nimauchunadminkerak})
    await message.answer(text='Telegram akauntingiz yoki nomeringizni qoldiring:\nadmining ozi siz bilan boglanadi', reply_markup=bekor)
    await rusadmin.akaunt.set()@dp.message_handler(state=admin.akaunt,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=russ)
    await state.finish()
@dp.message_handler(state=rusadmin.akaunt)
async def bot_echo(message: types.Message,state: FSMContext):
    akaunt = message.text
    await state.update_data({'akaunt': akaunt})

    data = await state.get_data()
    nimauchunadminkerak = data.get('nimauchunadminkerak')
    akaunt = data.get('akaunt')

    matn = f"ADMIN BILAN BOGLANISH: \n\n👤Nima uchun admin kerakligi:{nimauchunadminkerak}\n" \
           f"📅Akaunt vs tel: {akaunt}\n"\

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugmaa)
    await rusadmin.admingayuborish.set()

@dp.message_handler(state=rusadmin.admingayuborish, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Yozgan habaringiz adminga yuborilmadi',reply_markup=russ)
    await state.finish()

@dp.message_handler(state=rusadmin.admingayuborish, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida siz bilan boglanamiz')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    nimauchunadminkerak = data.get('nimauchunadminkerak')
    akaunt = data.get('akaunt')



    matn +=f'Nima uchun admin kerakligi: {nimauchunadminkerak}\n'\
           f'Akaunt yoki telefon nomer: {akaunt}\n'\

    await message.answer(text='.', reply_markup=russ)
    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=russ)
    await state.finish()