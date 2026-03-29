import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.getenv("BOT_TOKEN") or "ВАШ_ТОКЕН"
ADMIN_IDS = [123456789]  # Гоша твой  ID для админки, измени под себя обязательно 

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Настройки уроков
LESSON_TIME = "14:00"  # Время отправки уроков можешь поставить любое 
TOTAL_LESSONS = 10     # Всего уроков в курсе