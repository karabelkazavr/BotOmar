from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint, choice
import os
from bs4 import BeautifulSoup
import requests
from config import TOKEN
from client_kb import kb_client
from aiogram import types, Dispatcher
import asyncio




async def bot_startup(_):
	print('Бот вышел в онлайн.')

random_page = randint(2 ,40)


url = f'https://stihionline.ru/rubai-omara-hajyama/page/{random_page}'
r = requests.get(url) 
soup = BeautifulSoup(r.text,'html.parser')

all_rubai = soup.find_all('div',class_='content-data')

clear_rubai = []
for i in all_rubai:
    clear_rubai.append(i.getText())
random_rubai = choice(clear_rubai)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!', reply_markup=kb_client)
		await message.delete()
	except:
		'except'


@dp.message_handler(commands=['Привет'])
async def command_open(message : types.Message):
	await bot.send_message(message.from_user.id, 'Хорошо, теперь, если хочешь услышать мудрость, напиши: мудрость.')
	await message.delete()


@dp.message_handler(commands=['мудрость'])
async def command_rubai(message : types.Message):
	await bot.send_message(message.chat.id, random_rubai)
	await message.delete()



def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(command_open, commands=['Привет'])
	dp.register_message_handler(command_rubai, commands=['мудрость'])
	


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup = bot_startup)