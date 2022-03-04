from aiogram import types
from aiogram.dispatcher import FSMContext

from states.botyasash import botyasash
from keyboards.default.almazlar import asosiy_tugma
from keyboards.default.tasdiqlash import asosiy
from loader import dp, bot


@dp.message_handler(text='Bot uchun zakas')
async def bot_echo(message: types.Message):
    await message.answer(text="O'zingiz haqingizda qisqacha malumot yozing:", reply_markup=bekor)
    await botyasash.ozingizhaqingizda.set()
@dp.message_handler(state=botyasash.ozingizhaqingizda, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="Bot yasatirish uchun zakas berish bekor qilindi", reply_markup=asosiy)
    await state.finish()


@dp.message_handler(state=botyasash.ozingizhaqingizda)
async def bot_echo(message: types.Message, state: FSMContext):
    ozingizhaqingizda = message.text
    await state.update_data({'ozingizhaqingizda': ozingizhaqingizda})
    await message.answer(text="Telegram bot haqida:\nG'oyangizni qisqacha yozib qoldiring",reply_markup=bekor)
    await botyasash.goya.set()
@dp.message_handler(state=botyasash.goya,text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=botyasash.goya)
async def bot_echo(message: types.Message, state: FSMContext):
    goya = message.text
    await state.update_data({'goya': goya})
    await message.answer(text='Telegram akauntingiz yoki nomeringizni qoldiring:\nadmining ozi siz bilan boglanadi',reply_markup=bekor)
    await botyasash.akaunt.set()

@dp.message_handler(state=botyasash.akaunt)
async def bot_echo(message: types.Message, state: FSMContext):
    akaunt = message.text
    await state.update_data({'akaunt': akaunt})

    data = await state.get_data()
    ozingizhaqingizda = data.get('ozingizhaqingizda')
    goya = data.get('goya')
    akaunt = data.get('akaunt')

    matn = f"Bot yasatirish uchun zakas berish: \n\n👤Ozingiz haqingizda qiqacha: {ozingizhaqingizda}\n" \
           f"G'oyangiz haqida qisqacha: {goya}\n"\
           f"Akaunt vs tel: {akaunt}\n"\

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing adminlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
    await botyasash.admingayuborish.set()


@dp.message_handler(state=botyasash.admingayuborish, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Yozgan habaringiz adminga yuborilmadi', reply_markup=asosiy)
    await state.finish()


@dp.message_handler(state=botyasash.admingayuborish, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida siz bilan boglanamiz')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ozingizhaqingizda = data.get('ozingizhaqingizda')
    goya = data.get('goya')
    akaunt = data.get('akaunt')

    matn +=f'Ozi haqida: {ozingizhaqingizda}\n'\
           f'Telegram bot uchun goyasi: {goya}\n'\
           f'Akaunt vs Tel: {akaunt}\n'\

    await message.answer(text='.', reply_markup=asosiy)
    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=asosiy)
    await state.finish()



from aiogram import types
from aiogram.dispatcher import FSMContext

from states.botyasash import rusbotyasash
from keyboards.default.kunlari import bekor
from keyboards.default.almazlar import asosiy_tugmaa
from keyboards.default.tasdiqlash import russ
from loader import dp, bot


@dp.message_handler(text='Bot uchun zakas')
async def bot_echo(message: types.Message):
    await message.answer(text="O'zingiz haqingizda qisqacha malumot yozing:", reply_markup=bekor)
    await rusbotyasash.ozingizhaqingizda.set()
@dp.message_handler(state=rusbotyasash.ozingizhaqingizda, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="Bot yasatirish uchun zakas berish bekor qilindi", reply_markup=russ)
    await state.finish()


@dp.message_handler(state=botyasash.ozingizhaqingizda)
async def bot_echo(message: types.Message, state: FSMContext):
    ozingizhaqingizda = message.text
    await state.update_data({'ozingizhaqingizda': ozingizhaqingizda})
    await message.answer(text="Telegram bot haqida:\nG'oyangizni qisqacha yozib qoldiring",reply_markup=bekor)
    await botyasash.goya.set()
@dp.message_handler(state=rusbotyasash.goya,text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="Admin bilan bog'lanish bekor qilindi", reply_markup=russ)
    await state.finish()
@dp.message_handler(state=rusbotyasash.goya)
async def bot_echo(message: types.Message, state: FSMContext):
    goya = message.text
    await state.update_data({'goya': goya})
    await message.answer(text='Telegram akauntingiz yoki nomeringizni qoldiring:\nadmining ozi siz bilan boglanadi',reply_markup=bekor)
    await rusbotyasash.akaunt.set()

@dp.message_handler(state=rusbotyasash.akaunt)
async def bot_echo(message: types.Message, state: FSMContext):
    akaunt = message.text
    await state.update_data({'akaunt': akaunt})

    data = await state.get_data()
    ozingizhaqingizda = data.get('ozingizhaqingizda')
    goya = data.get('goya')
    akaunt = data.get('akaunt')

    matn = f"Bot yasatirish uchun zakas berish: \n\n👤Ozingiz haqingizda qiqacha: {ozingizhaqingizda}\n" \
           f"G'oyangiz haqida qisqacha: {goya}\n"\
           f"Akaunt vs tel: {akaunt}\n"\

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing adminlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugmaa)
    await rusbotyasash.admingayuborish.set()


@dp.message_handler(state=rusbotyasash.admingayuborish, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Yozgan habaringiz adminga yuborilmadi', reply_markup=russ)
    await state.finish()


@dp.message_handler(state=rusbotyasash.admingayuborish, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida siz bilan boglanamiz')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ozingizhaqingizda = data.get('ozingizhaqingizda')
    goya = data.get('goya')
    akaunt = data.get('akaunt')

    matn +=f'Ozi haqida: {ozingizhaqingizda}\n'\
           f'Telegram bot uchun goyasi: {goya}\n'\
           f'Akaunt vs Tel: {akaunt}\n'\

    await message.answer(text='.', reply_markup=russ)
    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=russ)
    await state.finish()


