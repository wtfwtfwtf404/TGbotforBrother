from config import bot, dp
import sqlite3
from datetime import datetime

# Простая SQLite база
def init_db():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        has_paid BOOLEAN DEFAULT 0,
        current_lesson INTEGER DEFAULT 0,
        last_lesson_date TEXT
    )
    ''')
    conn.commit()
    conn.close()

# CRUD операции
def get_user(user_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, **kwargs):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    if not get_user(user_id):
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
    
    set_clause = ', '.join([f"{k} = ?" for k in kwargs.keys()])
    values = list(kwargs.values()) + [user_id]
    cursor.execute(f'UPDATE users SET {set_clause} WHERE user_id = ?', values)
    conn.commit()
    conn.close()

# Инициализация при старте
init_db()