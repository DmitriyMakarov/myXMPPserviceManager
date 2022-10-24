import telebot
import config
from core.service import DataBase as db
from core.bot import botMenus
from res.strings import messages_strings
from core.service import accountsManager as am
from core.service import xmppApi as api
from core.service import UserPasswordGenerator as upg

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
            if db.newAccount(message.message.chat.id, am.newAccount()[0], am.newAccount()[1]) == 'ok':
                lang = db.checkUserLang(message.message.chat.id)
                msg = messages_strings.accounts[f'new_user_info_{lang}'] + f'<code>{db.getXmppAccountInfo(message.message.chat.id)[1]}@im.ydns.eu</code>' +'\n' + messages_strings.accounts[f'new_user_pas_{lang}'] + '<code>' + db.getXmppAccountInfo(message.message.chat.id)[2] + '</code>\n\n' + messages_strings.accounts[f'new_account_next_{lang}']
                bot.send_message(message.message.chat.id, msg, parse_mode="HTML")
                api.addAccount(db.getXmppAccountInfo(message.message.chat.id)[1], db.getXmppAccountInfo(message.message.chat.id)[2])
        elif db.getXmppAccountInfo(message.message.chat.id)[0] == 'ok':
            bot.send_message(message.message.chat.id, messages_strings.accounts[f'newuser_error_{db.checkUserLang(message.message.chat.id)}'])

    elif message.data == 'passwd':
        if db.getXmppAccountInfo(message.message.chat.id)[0] != 'err':
            am.changePassword(message.message.chat.id)
            bot.send_message(message.message.chat.id, messages_strings.password[
                f'new_pas_msg_{db.checkUserLang(message.message.chat.id)}'] + '<code>' + db.getXmppAccountInfo(message.message.chat.id)[2] + '</code>',
                             parse_mode='HTML')
        elif db.getXmppAccountInfo(message.message.chat.id)[0] == 'err':
            bot.send_message(message.message.chat.id, messages_strings.password[f'new_pas_err_msg_{db.checkUserLang(message.message.chat.id)}'])

    elif message.data == 'remove':
        if db.getXmppAccountInfo(message.message.chat.id)[0] != 'err':
            am.removeAccount(message.message.chat.id)
            bot.send_message(message.message.chat.id, messages_strings.accounts[f'del_account_{db.checkUserLang(message.message.chat.id)}'])
        else:
            bot.send_message(message.message.chat.id, messages_strings.password[f'new_pas_err_msg_{db.checkUserLang(message.message.chat.id)}'])

    elif message.data == 'settings':
        botMenus.settingsMenu(message.message.chat.id, db.checkUserLang(message.message.chat.id))

bot.infinity_polling()