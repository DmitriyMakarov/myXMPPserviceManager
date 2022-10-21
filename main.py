import config
import sqlite3
from res.strings import service_strings
from core.bot import bot


try:
    cfg = config.Config('res/configs/config.cfg')
    bot()
except FileNotFoundError as error:
    print(service_strings.init_tests['no_config_file'])
    exit(error)

try:
    sqlite_connection = sqlite3.Connection('res/base.db')
    cursor = sqlite_connection.cursor()
    print('База данных инициализирована')
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()
except sqlite3.Error as error:
    print('Ошибка при подключении к базеданных', error)