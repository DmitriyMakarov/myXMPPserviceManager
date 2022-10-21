import sqlite3
import telebot
import config

from core.bot import bot as b
from res.strings import service_string


try:
    cfg = config.Config('res/configs/config.cfg')
except FileNotFoundError as err:
    print(f'\n{service_string.init_tests["no_config_file"]}')
    exit(err)

bot = telebot.TeleBot(cfg.token)

try:
    sqlite_connection = sqlite3.Connection('res/base/base.db')
    cursor = sqlite_connection.cursor()
    print('База данных инициализирована')
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()
except sqlite3.Error as error:
    print('Ошибка при подключении к базеданных')
    exit(error)

b()

def __init__():

    return
