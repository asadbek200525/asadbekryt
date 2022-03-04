from aiogram import types
from aiogram.dispatcher import FSMContext

from states.Vaucher import Vaucher
from keyboards.default.tolov import tola
from keyboards.default.vauchervaqti import vaqti
from keyboards.default.kunlari import bekor
from keyboards.default.almazlar import asosiy_tugma
from keyboards.default.tasdiqlash import asosiy
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Vaucher💳')
async def bot_echo(message: types.Message):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza berish \n \nɪsᴍ ꜰᴀᴍɪʟʏᴀɴɢɪᴢɴɪ ᴋɪʀɪᴛɪɴɢ',reply_markup=bekor)
    await Vaucher.ism_fam.set()
@dp.message_handler(state=Vaucher.ism_fam,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Vaucher.ism_fam)
async def bot_echo(message: types.Message,state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})

    await message.answer(text='📞𝗔𝗹𝗼𝗾𝗮\n\nBoglanish uchun raqamingizni kiriting?\nMasalan:+998 91 515 94 43',reply_markup=bekor)
    await Vaucher.nomer.set()
@dp.message_handler(state=Vaucher.nomer,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Vaucher.nomer)
async def bot_echo(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data({'nomer':nomer})
    await message.answer(text='Tolov turini kiriting\n\nMasalan:Kartaga yoki Qiwi kashalokka boshqa turdagi tolovlarni qabul qilmaymiz',reply_markup=tola)
    await Vaucher.tolov.set()
@dp.message_handler(state=Vaucher.nomer,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Vaucher.tolov)
async def bot_echo(message: types.Message, state: FSMContext):
    tolov = message.text
    await state.update_data({'tolov': tolov})

    await message.answer(text='ꜰʀᴇᴇ ꜰɪʀᴇ ɪᴅʏɪɴɢɪᴢɴɪ ᴋɪʀɪᴛɪɴɢ',reply_markup=bekor)
    await Vaucher.ffid.set()
@dp.message_handler(state=Vaucher.ffid,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Vaucher.ffid)
async def bot_echo(message: types.Message, state: FSMContext):
    ffid = message.text
    await state.update_data({'ffid':ffid})
    await message.answer(text='vaucherlar',reply_markup=vaqti)
    await Vaucher.Vauncher.set()
@dp.message_handler(state=Vaucher.Vauncher,text='Bekor qilish')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Vaucher💳 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
    await state.finish()
@dp.message_handler(state=Vaucher.Vauncher)
async def bot_echo(message: types.Message, state: FSMContext):
    Vauncher = message.text
    await state.update_data({'Vauncher':Vauncher})


    data = await state.get_data()
    ism = data.get('ism')
    nomer = data.get('nomer')
    tolov = data.get('tolov')
    ffid = data.get('ffid')
    Vauncher = data.get('Vauncher')

    matn = f"Vaucher💳:\n\n👤Ismingiz :{ism}\n"\
           f"📞Aloqa :{nomer}\n"\
           f"💰Tolov :{tolov}\n"\
           f"🎮Id_Free Fire :{ffid}\n"\
           f"💳Vaucher :{Vauncher}"

    await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
    await Vaucher.Tastiqlash.set()

@dp.message_handler(state=Vaucher.Tastiqlash, text='Bekor qilish')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bekor qilindi',reply_markup=asosiy)
    await state.finish()

@dp.message_handler(state=Vaucher.Tastiqlash, text='Tasdiqlash')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Adminga yuborildi yaqin vaqt ichida danaterlarimiz siz bilan boglanishadi')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ism = data.get('ism')
    nomer = data.get('nomer')
    tolov = data.get('tolov')
    ffid = data.get('ffid')
    Vauncher = data.get('Vauncher')

    matn +=f'ISMI :{ism}\n'\
           f'NOMERI :{nomer}\n'\
           f'TOLOV TURI :{tolov}\n'\
           f'FREE FIRE IDSI :{ffid}\n'\
           f'VAUNCHER :{Vauncher}\n'\


    await message.answer(text='.',reply_markup=asosiy)
    await bot.send_message(chat_id=1035757120, text=matn,reply_markup=asosiy)
    await state.finish()



from aiogram import types
from aiogram.dispatcher import FSMContext

from states.Vaucher import RusVaucher
from keyboards.default.tolov import tolaa
from keyboards.default.vauchervaqti import vaqtii
from keyboards.default.rusbekor import rusbekor
from keyboards.default.almazlar import asosiy_tugmaa
from keyboards.default.tasdiqlash import russ
from loader import dp, bot


# Echo bot
@dp.message_handler(text='Ваучер💳')
async def bot_echo(message: types.Message):
    await message.answer(text='Подать заявку на ваучер\n \nВведите свое имя и фамилию',reply_markup=rusbekor)
    await RusVaucher.ism_fam.set()

@dp.message_handler(state=RusVaucher.ism_fam,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку ваучера отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusVaucher.ism_fam)
async def bot_echo(message: types.Message,state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})

    await message.answer(text='📞Введите свой номер',reply_markup=rusbekor)
    await RusVaucher.nomer.set()

@dp.message_handler(state=RusVaucher.nomer,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку ваучера отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusVaucher.nomer)
async def bot_echo(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data({'nomer':nomer})
    await message.answer(text='Введите тип платежа',reply_markup=tolaa)
    await RusVaucher.tolov.set()

@dp.message_handler(state=RusVaucher.tolov,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку ваучера отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusVaucher.tolov)
async def bot_echo(message: types.Message, state: FSMContext):
    tolov = message.text
    await state.update_data({'tolov': tolov})

    await message.answer(text='Введите свой Free Fire ID',reply_markup=rusbekor)
    await RusVaucher.ffid.set()

@dp.message_handler(state=RusVaucher.ffid,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку ваучера отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusVaucher.ffid)
async def bot_echo(message: types.Message, state: FSMContext):
    ffid = message.text
    await state.update_data({'ffid':ffid})
    await message.answer(text='ваучеры',reply_markup=vaqtii)
    await RusVaucher.Vauncher.set()

@dp.message_handler(state=RusVaucher.nomer,text='🔙Отменит')
async def bot_echo(message: types.Message,state: FSMContext):
    await message.answer(text='Заявка на покупку ваучера отменена', reply_markup=russ)
    await state.finish()

@dp.message_handler(state=RusVaucher.Vauncher)
async def bot_echo(message: types.Message, state: FSMContext):
    Vauncher = message.text
    await state.update_data({'Vauncher':Vauncher})


    data = await state.get_data()
    ism = data.get('ism')
    nomer = data.get('nomer')
    tolov = data.get('tolov')
    ffid = data.get('ffid')
    Vauncher = data.get('Vauncher')

    matn = f"Ваучер💳:\n\n👤Ваше имя :{ism}\n"\
           f"📞Номер:{nomer}\n"\
           f"💰Оплата :{tolov}\n"\
           f"🎮Id_Free Fire :{ffid}\n"\
           f"💳Ваучер :{Vauncher}"

    await message.answer(text=f'{matn}\nЕсли все пойдет хорошо, нажмите «Подтвердить», и наши танцоры свяжутся с вами.',reply_markup=asosiy_tugmaa)
    await Vaucher.Tastiqlash.set()

@dp.message_handler(state=Vaucher.Tastiqlash, text='Отмена')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отменено',reply_markup=russ)
    await state.finish()

@dp.message_handler(state=Vaucher.Tastiqlash, text='Подтвердить')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отправлено admin В ближайшее время наши танцоры свяжутся с вами')

    username = message.from_user.username

    matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    ism = data.get('ism')
    nomer = data.get('nomer')
    tolov = data.get('tolov')
    ffid = data.get('ffid')
    Vauncher = data.get('Vauncher')

    matn +=f'ISMI :{ism}\n'\
           f'NOMERI :{nomer}\n'\
           f'TOLOV TURI :{tolov}\n'\
           f'FREE FIRE IDSI :{ffid}\n'\
           f'VAUNCHER :{Vauncher}\n'\


    await message.answer(text='.',reply_markup=russ)
    await bot.send_message(chat_id=1035757120, text=matn,reply_markup=russ)
    await state.finish()








