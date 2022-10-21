import telebot
import config
from core.service import DataBase as db
from core.bot import botMenus

cfg = config.Config('res/configs/config.cfg')
bot = telebot.TeleBot(cfg.token)


@bot.message_handler(commands=['start'])
def start(message):
    if db.checkBotUserExist(message.chat.id) is None:
        if db.addBotUser(message.chat.id) is not None:
            botMenus.menuLangSelect(message.chat.id)

    elif db.checkBotUserExist(message.chat.id) == 'error':
        print('Error')

    else:
        if db.checkUserLang(message.chat.id) != 'None':
            botMenus.mainMenu(message.chat.id, db.checkUserLang(message.chat.id))
        else:
            botMenus.menuLangSelect(message.chat.id)
#        botMenus.showMainMenu(message.chat.id, 'RU')


@bot.callback_query_handler(func=lambda call: True)
def callbackHandler(message):
    if message.data == 'RU' or 'EN':
        if db.setBotUserLang(message.message.chat.id, message.data) == 'ok':
            botMenus.mainMenu(message.message.chat.id, db.checkUserLang(message.message.chat
                                                                        .id))

bot.infinity_polling()