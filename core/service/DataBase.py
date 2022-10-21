import sqlite3


sql_connection = sqlite3.connect('res/base/base.db', check_same_thread=False)

def checkBotUserExist(user_id):
    try:
        cursor = sql_connection.cursor()
        query = 'SELECT id FROM users WHERE user_id=' + str(user_id)
        cursor.execute(query)
        result = str(cursor.fetchall())
        if len(result) > 2:
            result = result.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(',', '')
        else:
            result = None
        print(result)
        cursor.close()
    except sqlite3.Error as error:
        result = 'error'
    return result

    return result


def checkUserLang(user_id):
    try:
        cursor = sql_connection.cursor()
        query_lang = f"SELECT user_lang FROM users WHERE user_id='{user_id}';"
        cursor.execute(query_lang)
        lang_f = cursor.fetchall()
        if len(lang_f) > 0:
            lang_check_result = str(lang_f[0]).replace('(', '').replace(')', '').replace(',', '').replace("'",
                                                                                                          "").replace(
                ' ', '')
        elif len(lang_f) == 0:
            lang_check_result = None
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    return lang_check_result


def addBotUser(user_id):
    try:
        cursor = sql_connection.cursor()
        query_new_user = f'INSERT INTO users (user_id) VALUES ({user_id});'
        cursor.execute(query_new_user)
        sql_connection.commit()
        cursor.close()
        result = ''
    except sqlite3.Error as err:
        print(err)
        result = None
    return result


def setBotUserLang(user_id, lang):
    try:
        cursor = sql_connection.cursor()
        query_lang = f"UPDATE users SET user_lang='{lang}' WHERE user_id='{user_id}'"
        cursor.execute(query_lang)
        sql_connection.commit()
        cursor.close()
        result = 'ok'
    except sqlite3.Error as error:
        result = error
    return result
