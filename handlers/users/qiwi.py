from aiogram import types
from aiogram.dispatcher import FSMContext

from states.qiwi import Qiwi
from keyboards.default.almazlar import asosiy_tugma
from keyboards.default.tasdiqlash import asosiy
from keyboards.default.kunlari import bekor
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Qiwi rub💰')
async def bot_echo(message: types.Message):
    await message.answer(text='Qiwi rub💰 sotib olish uchun ariza berish \n \nɪsᴍ ꜰᴀᴍɪʟʏᴀɴɢɪᴢɴɪ ᴋɪʀɪᴛɪɴɢ',reply_markup=bekor)
    await Qiwi.ism_fam.set()
@dp.message_handler(state=Qiwi.ism_fam,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi rubl💰 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Qiwi.ism_fam)
async def bot_echo(message: types.Message,state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})

    await message.answer(text='Yoshingizni kiriting',reply_markup=bekor)
    await Qiwi.yoshi.set()
@dp.message_handler(state=Qiwi.yoshi,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi rubl💰 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Qiwi.yoshi)
async def bot_echo(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data({'yoshi':yoshi})
    await message.answer(text='Qancha rubl sotib olmoqchisz',reply_markup=bekor)
    await Qiwi.qancha.set()
@dp.message_handler(state=Qiwi.qancha,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi rubl💰 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Qiwi.qancha)
async def bot_echo(message: types.Message, state: FSMContext):
    qancha = message.text
    await state.update_data({'qancha': qancha})
    await message.answer(text='📞𝗔𝗹𝗼𝗾𝗮\n\nBoglanish uchun raqamingizni kiriting?\nMasalan:+998 91 515 94 43',reply_markup=bekor)
    await Qiwi.aloqa.set()
@dp.message_handler(state=Qiwi.aloqa,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi rubl💰 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Qiwi.aloqa)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data({'aloqa': aloqa})
    await message.answer(text='Qiwi raqamangizni kiriting',reply_markup=bekor)
    await Qiwi.Qwiraqam.set()
@dp.message_handler(state=Qiwi.Qwiraqam,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Qiwi rubl💰 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Qiwi.Qwiraqam)
async def bot_echo(message: types.Message, state: FSMContext):
    Qiwiraqam = message.text
    await state.update_data({'Qiwiraqam':Qiwiraqam})


    data = await state.get_data()
    ism = data.get('ism')
    yoshi = data.get('yoshi')
    qancha = data.get('qancha')
    aloqa = data.get('aloqa')
    Qiwiraqam = data.get('Qiwiraqam')

    matn = f"Qiwi rub💰:\n\n👤Ismingiz :{ism}\n"\
           f"📅Yoshingiz :{yoshi}\n"\
           f"💰Qancha rubl kerakligi :{qancha}\n"\
           f"📞Aloqa :{aloqa}\n"\
           f"💳Qiwi raqamingiz :{Qiwiraqam}"

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
    await Qiwi.tasdiq.set()

@dp.message_handler(state=Qiwi.tasdiq, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bekor qilindi',reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Qiwi.tasdiq, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida danaterlarimiz siz bilan boglanishadi')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ism = data.get('ism')
    yoshi = data.get('yoshi')
    qancha = data.get('qancha')
    aloqa = data.get('aloqa')
    Qiwiraqam = data.get('Qiwiraqam')

    matn += f"Qiwi rub💰:\n\n👤Ismingiz :{ism}\n"\
           f"📅Yoshi :{yoshi}\n"\
           f"💰Qancha rubl kerakligi :{qancha}\n"\
           f"📞Aloqa :{aloqa}\n"\
           f"💳Qiwi raqami :{Qiwiraqam}"


    await message.answer(text='🔎',reply_markup=asosiy)
    await bot.send_message(chat_id=1035757120, text=matn,reply_markup=asosiy)
    await state.finish()



from aiogram import types
from aiogram.dispatcher import FSMContext

from states.qiwi import RusQiwi
from keyboards.default.almazlar import asosiy_tugmaa
from keyboards.default.tasdiqlash import russ
from keyboards.default.rusbekor import rusbekor
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Киви руб💰')
async def bot_echo(message: types.Message):
    await message.answer(text='Подать заявку на Киви руб💰 \n \nɪsᴍ ꜰᴀᴍɪʟʏᴀɴɢɪᴢɴɪ ᴋɪʀɪᴛɪɴɢ',reply_markup=rusbekor)
    await Qiwi.ism_fam.set()
@dp.message_handler(state=RusQiwi.ism_fam,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку Киви рублей отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.ism_fam)
async def bot_echo(message: types.Message,state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})

    await message.answer(text='Введите свой возраст',reply_markup=rusbekor)
    await RusQiwi.yoshi.set()

@dp.message_handler(state=RusQiwi.yoshi,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку Киви рублей отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.yoshi)
async def bot_echo(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data({'yoshi':yoshi})
    await message.answer(text='Qancha rubl sotib olmoqchisz',reply_markup=rusbekor)
    await RusQiwi.qancha.set()

@dp.message_handler(state=RusQiwi.qancha,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку Киви рублей отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.qancha)
async def bot_echo(message: types.Message, state: FSMContext):
    qancha = message.text
    await state.update_data({'qancha': qancha})
    await message.answer(text='Введите свой номер для связи с вами:',reply_markup=rusbekor)
    await RusQiwi.aloqa.set()

@dp.message_handler(state=RusQiwi.aloqa,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку Киви рублей отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.aloqa)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data({'aloqa': aloqa})
    await message.answer(text='Qiwi raqamangizni kiriting',reply_markup=rusbekor)
    await RusQiwi.Qwiraqam.set()

@dp.message_handler(state=RusQiwi.Qwiraqam,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку Киви рублей отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.Qwiraqam)
async def bot_echo(message: types.Message, state: FSMContext):
    Qiwiraqam = message.text
    await state.update_data({'Qiwiraqm':Qiwiraqam})


    data = await state.get_data()
    ism = data.get('ism')
    yoshi = data.get('yoshi')
    qancha = data.get('qancha')
    aloqa = data.get('aloqa')
    Qiwiraqam = data.get('Qiwiraqam')

    matn = f"Киви руб💰:\n\n👤👤имя :{ism}\n"\
           f"📅возраст :{yoshi}\n"\
           f"💰Qancha rubl kerakligi :{qancha}\n"\
           f"📞Твой номер  :{aloqa}\n"\
           f"💳Qiwi raqamingiz :{Qiwiraqam}"

    await message.answer(text=f'{matn}\nЕсли все пойдет хорошо, нажмите «Подтвердить», и наши танцоры свяжутся с вами.',reply_markup=asosiy_tugmaa)
    await RusQiwi.tasdiq.set()

@dp.message_handler(state=RusQiwi.tasdiq, text='Отмена')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отменено',reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusQiwi.tasdiq, text='Подтвердить')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отправлено admin В ближайшее время наши танцоры свяжутся с вами')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ism = data.get('ism')
    yoshi = data.get('yoshi')
    qancha = data.get('qancha')
    aloqa = data.get('aloqa')
    Qiwiraqam = data.get('Qiwiraqam')

    matn += f"Киви руб💰:\n\n👤👤имя :{ism}\n"\
           f"📅возраст :{yoshi}\n"\
           f"💰Qancha rubl kerakligi :{qancha}\n"\
           f"📞Твой номер  :{aloqa}\n"\
           f"💳Qiwi raqamingiz :{Qiwiraqam}"


    await message.answer(text='🔎',reply_markup=russ)
    await bot.send_message(chat_id=1035757120, text=matn,reply_markup=russ)
    await state.finish()



