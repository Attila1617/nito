import requests
import logging

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer('Hello! This is nito. I provide the information about music theory. Type /help for instructions.')


@dp.message_handler(commands='help')
async def send_list_of_commands(message: types.Message):

    inline_btn_1 = InlineKeyboardButton('Music theory basics', callback_data='Music theory basics')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

    await message.answer('You can choose the topic', reply_markup=inline_kb1)


@dp.callback_query_handler(lambda c: c.data == 'Music theory basics')
async def process_callback_button1(callback_query: types.CallbackQuery):

    inline_btn_1 = InlineKeyboardButton('Sound concepts', callback_data='Sound concepts')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'The music theory basics include', reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)