from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database.db import database
from markup.markup import start, stop, config
from parser_cr import parser2
import asyncio
import threading


class FSM(StatesGroup):
    timing = State()
    crypto = State()
    run = State()
    stp = State()


async def cnfig(call: types.CallbackQuery):
    await call.message.answer("⏱ Время задержки перед отправкой сообщения(в секундах): ")
    await FSM.timing.set()

async def timing(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        database.timing(message.text, message.from_user.id)
        await state.finish()
        await message.answer("Бот настроен", reply_markup=start)

    else:
        await message.answer("Введите число!")




async def run_p(message: types.Message):
    global sostoyanie
    timing = database.get_timing(message.from_user.id)[0]
    if message.text == "✅ Запустить бота":
        sostoyanie = True
        await message.answer("Бот запущен!")
        while sostoyanie:
            price = parser2.crypto()
            await message.answer(price, reply_markup=stop)
            await asyncio.sleep(timing)

    if message.text == "❌ Остановить бота":
        sostoyanie = False
        await message.answer("Бот остановлен. Перейти к настройке", reply_markup=config)


# async def stop_p(message: types.Message):
#     global sostoyanie
#
#
# sostoyanie = True
# async def parser(message: types.Message):
#




def register_handlers(dp : Dispatcher):
    dp.register_callback_query_handler(cnfig, text="config", state=None)
    dp.register_message_handler(timing, state=FSM.timing)
    dp.register_message_handler(run_p)
    # dp.register_message_handler(stop_p)
    # dp.register_message_handler(parser)
