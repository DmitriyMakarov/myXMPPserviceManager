import telebot
from telebot import types
import config
from res.strings import bot_menu_strings as strings


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
    print(lang)