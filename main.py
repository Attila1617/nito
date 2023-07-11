import requests
import logging
import aiogram

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6383505659:AAGzImP9ELdAeY1VrSflJba1gfSw9Qck0G0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer('Hello! This is nito. I will provide the information about music and music theory.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)