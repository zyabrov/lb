from flask import Flask
from adminbot import tg_bot

app = Flask(__name__)
app.register_blueprint(tg_bot,url_prefix="/tg_bot")