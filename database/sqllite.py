import sqlite3

from config_data.config import PATH_TO_DATABASE


# Устанавливаем соединение с базой данных


def start_db():
    conn = sqlite3.connect(PATH_TO_DATABASE)
    cursor = conn.cursor()
    # Создаем таблицу "users"
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       userid TEXT)''')
    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()
