import asyncio

import aiogram.types
from aiogram.utils import exceptions
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from message_generate import *

bot = Bot(TOKEN_API, parse_mode=aiogram.types.ParseMode.HTML)
dp = Dispatcher(bot)


async def start_bot(_):
    db_start()
    print("Я запущен")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    chat_id = message.chat.id
    if is_chat_in_db(chat_id):
        try:
            await bot.delete_message(chat_id, get_msg_id(chat_id))
        except exceptions.MessageToDeleteNotFound:
            pass
        msg = await bot.send_message(chat_id,
                                     text=message_start(),
                                     reply_markup=ikb_start)
        null_user(chat_id, msg.message_id)
    else:
        msg = await bot.send_message(message.chat.id,
                                     text=message_start(),
                                     reply_markup=ikb_start)
        create_matrix_for_new_chat(chat_id, msg.message_id)
    await message.delete()


@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    msg = await bot.send_message(message.chat.id, text=message_help())
    await message.delete()
    await asyncio.sleep(8)
    await msg.delete()


@dp.message_handler(commands=['description'])
async def start_command(message: types.Message):
    msg = await bot.send_message(message.chat.id, text=message_description())
    await message.delete()
    await asyncio.sleep(8)
    await msg.delete()


@dp.message_handler()
async def echo_bot(message: types.Message):
    msg_id = get_msg_id(message.chat.id)
    text, keyboard = message_answer(message)
    if text != '-1':
        try:
            await bot.edit_message_text(text, message.chat.id, msg_id, reply_markup=keyboard)
        except:
            pass
    await message.delete()


@dp.callback_query_handler()
async def callback_handler(callback: types.CallbackQuery):
    msg = callback.message
    text, keyboard = callback_answer(callback)
    try:
        await msg.edit_text(text=text, reply_markup=keyboard)
    except exceptions.MessageNotModified:
        pass
    await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start_bot, skip_updates=True)
