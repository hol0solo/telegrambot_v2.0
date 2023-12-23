from loader import bot
import sqlite3
from config_data.config import PATH_TO_DATABASE


@bot.message_handler(commands=['history'])
def get_history(message):
    conn = sqlite3.connect(PATH_TO_DATABASE)
    cursor = conn.cursor()
    table_name = 'users_info'
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    result = cursor.fetchone()
    if result:
        cursor.execute("SELECT command, city, hotels_name "
                       "FROM users_info WHERE user_id = {}".format(message.from_user.id))
        rows = cursor.fetchall()
        for row in rows:
            total_info = []
            for info in row:
                total_info.append(info)
            bot.send_message(message.from_user.id, 'Введенная команда: {}\nЗапрошенный город: {}\n'
                                                   'Отели в городе {}'.format(total_info[0], total_info[1],
                                                                              total_info[2]))
    else:
        bot.send_message(message.from_user.id, "У вас нет истории")
    conn.close()
