import telebot
import config

cfg = config.Config('res/configs/config.cfg')
bot = telebot.TeleBot(cfg.token)
print('bot')
bot.infinity_polling()