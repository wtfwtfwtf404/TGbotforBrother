from aiogram import executor
from config import dp
from handlers import *
import asyncio
import logging

async def on_startup(_):
    asyncio.create_task(send_lessons())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    #try:
    #     asyncio.run(bot())
    # except KeyboardInterrupt:
    #     print("Бот выключен") 
    # Объясню, если ты будешь тестить бота без выгрузки на сервер /
    # то эта хуйня скроет ошибку, когда ты будешь выключать бота
    # По факту, если выгрузка на сервер будет, то это бесполезно, поэтому в комментах валяется 