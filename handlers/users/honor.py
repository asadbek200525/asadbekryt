from aiogram import types
from keyboards.default.honor import honor
from loader import dp


# Echo bot
@dp.message_handler(text='Honor๐ฎ')
async def bot_echo(message: types.Message):
    await message.answer(text='๐น ๐ด ๐ต  ๐ณ ๐ฆ ๐ธ ๐น ๐ท ๐ด ๐พ ๐ฐ ๐ฆ  ๐ญ ๐ด ๐ณ ๐ด ๐ท โ',reply_markup=honor)
