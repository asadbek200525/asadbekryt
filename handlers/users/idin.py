from aiogram import types
from aiogram.dispatcher import FSMContext

from states.idinfikatsiya import idinfikatsiyaaa
from keyboards.default.kunlari import bekor
from keyboards.default.almazlar import asosiy_tugma
from keyboards.default.tasdiqlash import asosiy
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Qiwi indinfikatsiya📣')
async def bot_echo(message: types.Message):
    await message.answer(text='Qiwi indinfikatsiya📣 qilish uchun ariza berish: \n\nɪsᴍ ꜰᴀᴍɪʟʏᴀɴɢɪᴢɴɪ ᴋɪʀɪᴛɪɴɢ',reply_markup=bekor)
    await idinfikatsiyaaa.ism.set()
@dp.message_handler(state=idinfikatsiyaaa.ism,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi indinfikatsiya📣 uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=idinfikatsiyaaa.ism)
async def bot_echo(message: types.Message,state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})

    await message.answer(text='Idinfikatsiya qilineydigon nomeringizni kiriting:',reply_markup=bekor)
    await idinfikatsiyaaa.idin.set()
@dp.message_handler(state=idinfikatsiyaaa.idin,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi indinfikatsiya📣 uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=idinfikatsiyaaa.idin)
async def bot_echo(message: types.Message, state: FSMContext):
    idin = message.text
    await state.update_data({'idin':idin})
    await message.answer(text='Siz bilan boglanishimz uchun nomeringini kiriting:',reply_markup=bekor)
    await idinfikatsiyaaa.aloqa.set()
@dp.message_handler(state=idinfikatsiyaaa.aloqa,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi indinfikatsiya📣 uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=idinfikatsiyaaa.aloqa)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data({'aloqa': aloqa})

    await message.answer(text='Telegram akauntingizni linkini bering:\n\n idinfikatsiya uchun',reply_markup=bekor)
    await idinfikatsiyaaa.tg.set()
@dp.message_handler(state=idinfikatsiyaaa.tg,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi indinfikatsiya📣 uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=idinfikatsiyaaa.tg)
async def bot_echo(message: types.Message, state: FSMContext):
    tg = message.text
    await state.update_data({'tg':tg})



    data = await state.get_data()
    ism = data.get('ism')
    idin = data.get('idin')
    aloqa = data.get('aloqa')
    tg = data.get('tg')

    matn = f"Qiwi indinfikatsiya📣:\n\n👤Ismingiz :{ism}\n"\
           f"📞Idinfikatsiya nomeringiz: {idin}\n"\
           f"📞Nomeringiz :{aloqa}\n"\
           f"🎮Telegram akauntingiz :{tg}\n"\


    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
    await idinfikatsiyaaa.tastiqlash.set()

@dp.message_handler(state=idinfikatsiyaaa.tastiqlash, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bekor qilindi',reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=idinfikatsiyaaa.tastiqlash, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida danaterlarimiz siz bilan boglanishadi')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ism = data.get('ism')
    idin = data.get('idin')
    aloqa = data.get('aloqa')
    tg = data.get('tg')


    matn +=f'ISMI :{ism}\n'\
           f'IDINFIKATSIYA QILINEDIGON NOMERI :{idin}\n'\
           f'ALOQA UCHUN NOMERI :{aloqa}\n'\
           f'TELEGRAM AKAUNTI :{tg}\n'\


    await message.answer(text='.',reply_markup=asosiy)
    await bot.send_message(chat_id=1035757120, text=matn,reply_markup=asosiy)
    await state.finish()







from aiogram import types
from aiogram.dispatcher import FSMContext

from states.idinfikatsiya import Rusidinfikatsiya
from keyboards.default.almazlar import asosiy_tugmaa
from keyboards.default.rusbekor import rusbekor
from keyboards.default.tasdiqlash import russ
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Идинфикация Киви📣')
async def bot_echo(message: types.Message):
    await message.answer(text='Подать заявку на идентификацию Киви📣: \n\nВведите свое имя и фамилию',reply_markup=rusbekor)
    await Rusidinfikatsiya.ismm.set()


@dp.message_handler(state=Rusidinfikatsiya.ismm, text='🔙Отменит')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Заявка на Индикацию Qiwi отменена', reply_markup=russ)
    await state.finish()


@dp.message_handler(state=Rusidinfikatsiya.ismm)
async def bot_echo(message: types.Message,state: FSMContext):
    ismm = message.text
    await state.update_data({'ismm': ismm})

    await message.answer(text='Введите свой идентификационный номер:',reply_markup=rusbekor)
    await Rusidinfikatsiya.idinn.set()


@dp.message_handler(state=Rusidinfikatsiya.idinn, text='🔙Отменит')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Заявка на Индикацию Qiwi отменена', reply_markup=russ)
    await state.finish()


@dp.message_handler(state=Rusidinfikatsiya.idinn)
async def bot_echo(message: types.Message, state: FSMContext):
    idinn = message.text
    await state.update_data({'idinn':idinn})
    await message.answer(text='Введите свой номер для связи с вами:',reply_markup=rusbekor)
    await Rusidinfikatsiya.aloqaa.set()

@dp.message_handler(state=Rusidinfikatsiya.aloqaa, text='🔙Отменит')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Заявка на Индикацию Qiwi отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=Rusidinfikatsiya.aloqaa)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqaa = message.text
    await state.update_data({'aloqaa': aloqaa})

    await message.answer(text='Дайте ссылку на ваш аккаунт Telegram:\n\nдля идентификации',reply_markup=rusbekor)
    await Rusidinfikatsiya.tgg.set()

@dp.message_handler(state=Rusidinfikatsiya.tgg, text='🔙Отменит')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Заявка на Индикацию Qiwi отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=Rusidinfikatsiya.tgg)
async def bot_echo(message: types.Message, state: FSMContext):
    tgg = message.text
    await state.update_data({'tgg':tgg})

    data = await state.get_data()
    ismm = data.get('ismm')
    idinn = data.get('idinn')
    aloqaa = data.get('aloqaa')
    tgg = data.get('tgg')

    matn = f"Идинфикация Киви📣:\n\n👤имя :{ismm}\n"\
           f"🎫Идентификационный номер: {idinn}\n"\
           f"📞Cвязи: {aloqaa}\n"\
           f"💾Telegram аккаунт: {tgg}\n"\

    await message.answer(text=f'{matn}\nЕсли все пойдет хорошо, нажмите «Подтвердить», и наши танцоры свяжутся с вами',reply_markup=asosiy_tugmaa)
    await Rusidinfikatsiya.tastiqlash.set()

@dp.message_handler(state=Rusidinfikatsiya.tastiqlash, text='Отмена')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отменено',reply_markup=russ)
    await state.finish()

@dp.message_handler(state=Rusidinfikatsiya.tastiqlash, text='Подтвердить')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отправлено admin В ближайшее время наши танцоры свяжутся с вами')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'


    data = await state.get_data()
    ismm = data.get('ismm')
    idinn = data.get('idinn')
    aloqaa = data.get('aloqaa')
    tgg = data.get('tgg')


    matn +=f'ISMI : {ismm}\n'\
           f'IDinn nomer : {idinn}\n'\
           f'TEL NOMEER : {aloqaa}\n'\
           f'TG AKAUNT : {tgg}\n'\

    await message.answer(text='.', reply_markup=russ)
    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=russ)
    await state.finish()













