from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_client = ReplyKeyboardMarkup()


b1 = KeyboardButton('/Привет')
b2 = KeyboardButton('/мудрость')

kb_client.add(b1).add(b2)