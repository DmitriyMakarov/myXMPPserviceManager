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


def getXmppAccountInfo(user_id):
    account = ''
    pas = ''
    try:
        cursor_acc = sql_connection.cursor()
        cursor_pas = sql_connection.cursor()
        query_account = f"SELECT account_name FROM accounts WHERE hidden=0 AND user_id IN (SELECT id FROM users WHERE user_id='{user_id}')"
        query_pas = f"SELECT password FROM accounts WHERE hidden=0 AND user_id IN (SELECT id FROM users WHERE user_id='{user_id}')"
        cursor_acc.execute(query_account)
        cursor_pas.execute(query_pas)
        result_acc = cursor_acc.fetchall()
        result_pas = cursor_pas.fetchall()
        if result_acc == []:
            func_result = 'err'
        else:
            func_result = 'ok'
            account = str(result_acc).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace('[',
                                                                                                                  '').replace(
                ']', '')
            pas = str(result_pas).replace('(', '').replace(')', '').replace("'", "").replace(',', '').replace('[',
                                                                                                              '').replace(
                ']', '')
            print('Account: ' + account + '\nPassword: ' + pas)
        cursor_acc.close()
        cursor_pas.close()
    except sqlite3.Error as err:
        print(err)
    return func_result, account, pas


def newAccount(user_id, user, password):
    try:
        cursor = sql_connection.cursor()
        queri_user_id = f"SELECT id FROM users WHERE user_id='{user_id}'"
        user_id_res = str(cursor.execute(queri_user_id).fetchall()[0]).replace('(', '').replace(')', '').replace(',',                                                                                                                 '')
        query_new_acc = f"INSERT INTO accounts (user_id, account_name, password) VALUES ('{user_id_res}', '{user}', '{password}')"
        cursor.execute(query_new_acc)
        sql_connection.commit()
        cursor.close()


    except sqlite3.Error as err:
        print(err)