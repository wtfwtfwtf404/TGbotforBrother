from aiogram import types
from config import bot, dp, TOTAL_LESSONS
from database import get_user, update_user
from keyboards import main_menu, payment_menu
import asyncio
from datetime import datetime

# Команда /start
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    user = get_user(message.from_user.id)
    if not user:
        update_user(message.from_user.id, has_paid=False)
    
    await message.answer("Привет! Я бот для обучения.", reply_markup=main_menu())

# Обработчики кнопок, почитай в скобках, что там и поймешь
@dp.callback_query_handler(lambda c: c.data == 'who_we_are')
async def who_we_are(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Мы - лучшая команда преподавателей!")

@dp.callback_query_handler(lambda c: c.data == 'buy_course')
async def buy_course(call: types.CallbackQuery):
    await call.answer()
    user = get_user(call.from_user.id)
    if user and user[1]:  # has_paid
        await call.message.answer("Вы уже купили курс!")
    else:
        await call.message.answer("Курс стоит 1000 руб.", reply_markup=payment_menu())

# Отправка уроков
async def send_lessons():
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == "14:00":  # Время из config.py
            # Здесь логика отправки уроков
            await asyncio.sleep(60)  # Чтобы не дублировалось
        await asyncio.sleep(10)  # Проверяем каждые 10 сек