from aiogram import Bot, Dispatcher, types, executor
from config import tokenn
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from markup.markup import config
from database.db import database
from handlers import handler


storage = MemoryStorage()
bot = Bot(tokenn)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def main(message: types.Message):
    database.user_registration(message.from_user.id)

    await message.answer(
        "Приветствую! Этот бот будет информировать вас о текущей цене трех основных криптовалют - bitcoin, ethereum, monero. Настройте его: ", reply_markup=config)

    handler.register_handlers(dp)



if __name__ == "__main__":
    executor.start_polling(dp)
