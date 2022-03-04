from aiogram import types
from aiogram.types import ContentType, InputFile
from loader import dp, bot


# Echo bot
@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[2].download()
    await message.answer(text='Rasm qabul qilindi')

@dp.message_handler(text='Nastroyka Irisa')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = InputFile(path_or_bytesio='photos/file_1.jpg')
    await bot.send_photo(chat_id=user_id,photo=video_manzil)

@dp.message_handler(text='Nastroka Sonik')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = InputFile(path_or_bytesio='photos/file_2.jpg')
    await bot.send_photo(chat_id=user_id,photo=video_manzil)

@dp.message_handler(text='Nastroyka Tandera')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = InputFile(path_or_bytesio='photos/file_3.jpg')
    await bot.send_photo(chat_id=user_id,photo=video_manzil)

@dp.message_handler(text='Nastroyka Funtika')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = InputFile(path_or_bytesio='photos/file_4.jpg')
    await bot.send_photo(chat_id=user_id,photo=video_manzil)

@dp.message_handler(text='Nastroyka Nindziya')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = InputFile(path_or_bytesio='photos/file_5.jpg')
    await bot.send_photo(chat_id=user_id,photo=video_manzil)
