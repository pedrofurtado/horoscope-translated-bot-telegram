import re
from flask import Flask, request
import telegram
import os

global bot
global HOROSCOPE_TRANSLATED_BOT_TELEGRAM_TOKEN
global URL

URL = os.getenv('TELEGRAM_BOT_URL')
HOROSCOPE_TRANSLATED_BOT_TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telegram.Bot(token=HOROSCOPE_TRANSLATED_BOT_TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Horoscope Translated Bot Telegram - See more details in https://github.com/pedrofurtado/horoscope-translated-bot-telegram'

@app.route('/get_me')
def get_me():
    return str(bot.get_me())

@app.route('/setup_webhook', methods=['GET', 'POST'])
def setup_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=HOROSCOPE_TRANSLATED_BOT_TELEGRAM_TOKEN))

    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

@app.route('/{}'.format(HOROSCOPE_TRANSLATED_BOT_TELEGRAM_TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    message_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()

    print('Telegram message received: Text [{message_text}] | Chat ID {chat_id} | Message ID {message_id} | Telegram object {telegram_object}'.format(message_text=text, chat_id=chat_id, message_id=message_id, telegram_object=repr(update)))

    if text == "/start":
        bot_welcome = """
        Welcome to HoroscopeTranslatedBot!
        """

        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=message_id)
    else:
        try:
            photo_url = "https://picsum.photos/200/300"
            bot.sendPhoto(chat_id=chat_id, photo=photo_url, reply_to_message_id=message_id)
        except Exception:
            bot.sendMessage(chat_id=chat_id, text="There was a problem!", reply_to_message_id=message_id)

    return 'ok'
