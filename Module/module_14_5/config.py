from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "7352979098:AAHNwqfR7pCtNDSHfJj-WKfM9h664jQhiDE"

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Рассчитать")
button2 = KeyboardButton("Информация")
button3 = KeyboardButton("Купить")
keyboard.add(button1, button2)
keyboard.add(button3)