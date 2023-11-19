import sys


sys.path.insert(1, 'Package/handlers')
sys.path.insert(1, 'Package')

from math import *
from config import *
from aiogram import Bot, Dispatcher
import asyncio
from datetime import datetime

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.message_handlers.once = False

@dp.message_handler(commands=['start'], commands_prefix='!/.')
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Ты негр? Или ты Влад?")
    await bot.send_sticker(message.chat.id,
                           sticker=r"CAACAgIAAxkBAAEFQzBizuacnkC1DjYSXB4Xh7ceiszPCAACBwIAAs9fiwd8QyU_jqqLjykE")