from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


config = InlineKeyboardMarkup(row_width=1)
btn = InlineKeyboardButton("⚙ Настройка бота", callback_data="config")
config.add(btn)

start = ReplyKeyboardMarkup(row_width=2)
start_btn = KeyboardButton("✅ Запустить бота")
start.add(start_btn)

stop = ReplyKeyboardMarkup(row_width=2)
stop_btn = KeyboardButton("❌ Остановить бота")
stop.add(stop_btn)