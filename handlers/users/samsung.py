from aiogram import types
from keyboards.default.samsung import samsung
from loader import dp


# Echo bot
@dp.message_handler(text='Samsung⚡')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡',reply_markup=samsung)

# Echo bot
@dp.message_handler(text='A10')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A10:\n\nобзор = 91 \nКоллиматор = 91 \n2x = 95\n4x = 93 \n8x = 10 ')

# Echo bot
@dp.message_handler(text='A20')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A20:\n\nОбзор 93\nКол 93\n2х 100\n4х 100 \n8х 50')

# Echo bot
@dp.message_handler(text='A20s')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A20s:\n\nОбзор = 100\nКоллиматор = 100\n2Х = 100 \n4Х = 100 \n8X = 50\nКнопка = 48\nDpi: 700')

@dp.message_handler(text='A30s')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A30s:\n\nобзор = 98\nКоллиматор = 100\n2x = 100\n4x = 100\n8x = 100\nКнопка = 75\n DPI = 411')

@dp.message_handler(text='A40')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A40\n\nобзор =100\nКоллиматор = 90\n2x = 90\n4x = 90\n8x = 0')

@dp.message_handler(text='A50')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A50\n\nобзор = 100\nКоллиматор = 100\n2x = 100\n4x = 90\n8x = 11')

@dp.message_handler(text='A60')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A60:\n\nОбзор = 91\nКол = 100\n2х = 71\n4х 824х = 82\n8х = 17\nКнопка = 55\nDPI = 597')

@dp.message_handler(text='A70')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A70:\n\nобзор = 80\nКоллиматор = 81\n2x = 61\n4x = 77\n8x = 19')

@dp.message_handler(text='A80')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A80:\n\nОбзор = 95 \nКол = 96\n2х = 97\n4х = 100 \n8х 0\nКнопка = 79\nDPI 600 ')

@dp.message_handler(text='A01')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A01: \n\nобзор = 98\nКоллиматор = 100\n2x = 90\n4x = 88\n8x = 29\nКнопка = 54')

@dp.message_handler(text='A8')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A8:\n\nОбзор=60\nКол=24\n2x=83\n4x=5\n8x=8\nDpi = 800')

@dp.message_handler(text='A6+')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A6+:\n\nОбзор = 44\nКол = 42\n2х = 80\n4х = 100\n8х = 50 ')

@dp.message_handler(text='A11')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A11:\n\nОбзор = 100\nКол=100\n2Х =100\n4Х =100\n8X =15\nКнопка  = 48 \nDPI = 740')

@dp.message_handler(text='A51')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A51:\n\nОбзор = 87\nКол = 86\n2х = 87\n4х = 87\n8х = 50')

@dp.message_handler(text='A7')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A7:\n\nОбзор = 100\nКол = 96\n2х = 84\n4х = 77\n8х = 16\nDPI = 650')

@dp.message_handler(text='A6')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A6: \n\nОбзор = 100\nКол = 95\n2х = 95\n4х = 80\n8х = 70\nКнопка = 90')

@dp.message_handler(text='A5 2017')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A5 2017:\n\nОбзор = 80\nКоллиматор = 100\n2x = 100\n4x = 100\n8x = 100\nКнопка = 65\nDPI = 480')

@dp.message_handler(text='A5')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A5:\n\nОбзор=99\nКол=100\n2Х =100\n4Х =100\n8X =15\nКнопка=62\nDPI = 455')

@dp.message_handler(text='J3')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ J3:\n\nобзор = 87\nКоллиматор = 60\n2x = 60\n4x = 55\n8x = 15')

@dp.message_handler(text='j7')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j7:\n\nобзор = 100\nКоллиматор = 100\n2x = 100\n4x = 100\n8x = 40')

@dp.message_handler(text='j5 Prime')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j5 Prime:\n\nобзор = 80\nКоллиматор = 100\n2x = 80\n4x = 60\n8x = 10')

@dp.message_handler(text='j2')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j2:\n\nобзор = 63\nКоллиматор = 100\n2x = 90\n4x = 90\n8x = 0')

@dp.message_handler(text='j4')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j4:\n\nобзор = 100\nКоллиматор = 90\n2x = 85\n4x = 85\n8x = 0')

@dp.message_handler(text='j6')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j6:\n\nОбзор = 100\nКол = 97\n2х = 92\n4х = 100\n8х = 49\nКнопка = 71\nDPI = 411')

@dp.message_handler(text='j6+')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j6+:\n\nОбзор = 93\nКол = 90\n2х = 70\n4х = 68\n8х = 50\nКнопка = 45')

@dp.message_handler(text='j4 Plus')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ j4 Plus:\n\nОбзор = 100\nКол = 100\n2х = 100\n4х = 100\n8х = 50\nКнопка = 61 ')

@dp.message_handler(text='S8')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ S8:\n\nОбзор = 100\nКоллиматор = 100\n2х = 100\n4х = 100\n8х = 100\nКнопка = 60\nDPI = 500')

@dp.message_handler(text='GALAXY GRAND PRIME')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ GALAXY GRAND PRIME:\n\nОбзор = 100\nКол = 100\n2х = 98\n4х = 100 \n8х = 50\nКнопка = 65')

@dp.message_handler(text='A30')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A30:\n\nОбзор = 98\nКол = 100\n2x = 96\n4x = 90\n8x = 33\nКнопка = 89')

@dp.message_handler(text='A12')
async def bot_echo(message: types.Message):
    await message.answer(text='Samsung⚡ A12:\n\nОбзор = 100\nКол = 100\n2x = 100\n4x = 100\n8x = 50')