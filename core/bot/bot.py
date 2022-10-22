import telebot
import config
from core.service import DataBase as db
from core.bot import botMenus
from res.strings import messages_strings
from core.service import accountsManager as am

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
            botMenus.showMainMenu(message.chat.id, db.checkUserLang(message.chat.id))
        else:
            botMenus.menuLangSelect(message.chat.id)
#        botMenus.showMainMenu(message.chat.id, 'RU')

@bot.message_handler(content_types=['text'])
def show_main_menu_handler(message):
    if message.text == 'ℹ️ Show Menu':
        botMenus.mainMenu(message.chat.id, db.checkUserLang(message.chat.id))
    elif message.text == 'ℹ️ Показать меню':
        botMenus.mainMenu(message.chat.id, db.checkUserLang(message.chat.id))


@bot.callback_query_handler(func=lambda call: True)
def callbackHandler(message):
    if message.data == 'RU':
        if db.setBotUserLang(message.message.chat.id, 'RU') == 'ok':
            botMenus.mainMenu(message.message.chat.id, db.checkUserLang(message.message.chat
                                                                        .id))
    elif message.data == 'EN':
        if db.setBotUserLang(message.message.chat.id, 'EN') == 'ok':
            botMenus.mainMenu(message.message.chat.id, db.checkUserLang(message.message.chat
                                                                        .id))
    elif message.data == 'info':
        if db.getXmppAccountInfo(message.message.chat.id)[0] == 'err':
            bot.send_message(message.message.chat.id, messages_strings.information[f'no_info_text_{db.checkUserLang(message.message.chat.id)}'])
        elif db.getXmppAccountInfo(message.message.chat.id)[0] != 'err':
            bot.send_message(message.message.chat.id,
                             messages_strings.information[f'info_text_{db.checkUserLang(message.message.chat.id)}'] + '\n' + '<code>' +
                             str(db.getXmppAccountInfo(message.message.chat.id)[1]) + '@im.ydns.eu</code>', parse_mode='HTML')

    elif message.data == 'help':
        bot.send_message(message.message.chat.id, messages_strings.help[f'help_main_{db.checkUserLang(message.message.chat.id)}'],
                         parse_mode='Markdown')

    elif message.data == 'newuser':
        if db.getXmppAccountInfo(message.message.chat.id)[0] == 'err':
            am.newAccount(message.message.chat.id)

bot.infinity_polling()