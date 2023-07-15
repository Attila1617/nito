import re
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
    await message.answer(
        'Hello! This is nito. I will provide the information about music theory from various sources of information on the Internet. Type /help for instructions.')


@dp.message_handler(commands='help')
async def send_list_of_commands(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Music theory basics', callback_data='Music theory basics')
    inline_btn_2 = InlineKeyboardButton('Intervals and scales', callback_data='Intervals and scales')
    inline_btn_3 = InlineKeyboardButton('Chord structure', callback_data='Chord structure')
    inline_btn_4 = InlineKeyboardButton('Song keys', callback_data='Song keys')

    inline_kb_full = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4)

    await message.answer('You can choose the topic', reply_markup=inline_kb_full)


@dp.callback_query_handler(lambda c: c.data == 'Music theory basics')
async def music_theory_basics(callback_query: types.CallbackQuery):
    inline_btn_1 = InlineKeyboardButton('Sound concepts', callback_data='Sound concepts')
    inline_btn_2 = InlineKeyboardButton('Music notes', callback_data='Music notes')
    inline_btn_3 = InlineKeyboardButton('How to read notes', callback_data='How to read notes')

    inline_kb_full = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3)

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'The music theory basics include', reply_markup=inline_kb_full)


@dp.callback_query_handler(lambda c: c.data == 'Sound concepts')
async def sound_concepts(callback_query: types.CallbackQuery):
    response = requests.get('https://www.music-theory.ru/index.php?option=com_content&view=article&id=4&Itemid=165&lang=ru').text
    result = re.search('<div class="item-page">', response)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
