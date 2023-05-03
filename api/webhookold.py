from flask import Flask, request
import telegram
import os
from myutils import funcs

global bot
bot = telegram.Bot(token=funcs.telegram_bot_token())

app = Flask(__name__)

@app.route('/')
def home():
    return 'Horoscope Translated Bot Telegram - See more details in https://github.com/pedrofurtado/horoscope-translated-bot-telegram'

@app.route('/get_me')
def get_me():
    return str(bot.get_me())

@app.route('/setup_webhook', methods=['GET', 'POST'])
def setup_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=funcs.telegram_bot_url(), HOOK=funcs.telegram_bot_token()))

    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

@app.route('/{}'.format(funcs.telegram_bot_token()), methods=['POST'])
def webhook():
    # https://github.com/python-telegram-bot/v13.x-wiki/wiki/Webhooks
    # https://github.com/aarzaary/telegram-bot-vercel-python/blob/48f1905bbfc0af25e11c376b817e9e91ba7e0174/example/bot.py#L15
    updater = funcs.create_updater()
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    updater.dispatcher.process_update(update)
    return 'ok'
