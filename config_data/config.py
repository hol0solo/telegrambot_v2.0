import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
PATH_TO_DATABASE = os.getenv("PATH_TO_DATABASE")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("lowprice", "Найти дешевые отели"),
    ("highprice", "Найти дорогие отели"),
    ("custom", "Найти отели по карману"),
    ("history", "История поиска")
)
