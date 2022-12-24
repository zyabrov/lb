import telebot
from flask import Blueprint
import credentials

tg_bot = Blueprint('tg_bot', __name__)

bot = telebot.TeleBot(credentials.bot_token)


class Webhook:
    def __init__(self, json_string):
        self.json_string = json_string

    def update(self):
        update = telebot.types.Update.de_json(self.json_string)
        bot.process_new_updates([update])
        print('update:', update)

