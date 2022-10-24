import telebot
from telebot import types
import config
from res.strings import bot_menu_strings as strings
from res.strings import messages_strings

cfg = config.Config('res/configs/config.cfg')
bot = telebot.TeleBot(cfg.token)


def showMainMenu(user_id, lang):
    mmenu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(strings.main_menu_buttons[f'show_main_menu_{lang}'])
    mmenu.add(button)
    bot.send_message(user_id, 'ℹ️ ', reply_markup=mmenu)


def menuLangSelect(user_id):
    markup = types.InlineKeyboardMarkup()
    buton_en = types.InlineKeyboardButton('🇺🇸 English', callback_data='EN')
    buton_ru = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='RU')
    markup.add(buton_en, buton_ru)
    bot.send_message(user_id, "Chosen language\nВыберете язык", reply_markup=markup)


def mainMenu(user_id, lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    mmenu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_info = types.InlineKeyboardButton('Info', callback_data='info')
    button_newuser = types.InlineKeyboardButton(strings.main_menu_buttons[f'm_menu_button_newuser_{lang}'],
                                                callback_data='newuser')
    button_passwd = types.InlineKeyboardButton(strings.main_menu_buttons[f'm_menu_button_passwd_{lang}'],
                                               callback_data='passwd')
    button_remove = types.InlineKeyboardButton(strings.main_menu_buttons[f'm_menu_button_remove_{lang}'],
                                               callback_data='remove')
    button_settings = types.InlineKeyboardButton(strings.main_menu_buttons[f'm_menu_button_settings_{lang}'],
                                                 callback_data='settings')
    button_help = types.InlineKeyboardButton(strings.main_menu_buttons[f'm_menu_button_help_{lang}'],
                                             callback_data='help')
    markup.add(button_info, button_newuser, button_passwd, button_remove, button_settings, button_help)
    button = types.KeyboardButton(strings.main_menu_buttons[f'show_main_menu_{lang}'])
    mmenu.add(button)
    bot.send_message(user_id,
                     messages_strings.information[f'main_about_{lang}'],
                     reply_markup=markup, parse_mode='HTML')


def settingsMenu(user_id, lang):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_about = types.InlineKeyboardButton(strings.settings_menu_buttons[f'about_client_{lang}'], callback_data='about_client', url='https://telegra.ph/Spisok-komand-bota-10-09')
    button_howLogin = types.InlineKeyboardButton(strings.settings_menu_buttons[f'how_login_{lang}'], callback_data='how_login')
    button_howPasChange = types.InlineKeyboardButton(strings.settings_menu_buttons[f'how_paschange_{lang}'], callback_data='how_pas')
    button_howCrypto = types.InlineKeyboardButton(strings.settings_menu_buttons[f'how_crypto_{lang}'], callback_data='how_crypto')
    markup.add(button_about, button_howLogin, button_howPasChange, button_howCrypto)
    bot.send_message(user_id, messages_strings.settings[f'settings_about_{lang}'], reply_markup=markup)