import re
from flask import Flask, request
import telegram
import os

global bot
global TOKEN
global URL

URL = os.getenv('TELEGRAM_BOT_URL')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Horoscope Translated Bot Telegram - See more details in https://github.com/pedrofurtado/horoscope-translated-bot-telegram'

@app.route('/setup_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN))

    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    telegram_message = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = telegram_message.message.chat.id
    message_id = telegram_message.message.message_id

    text = telegram_message.message.text.encode('utf-8').decode()

    print('Telegram message received: Text [{message_text}] | Chat ID {chat_id} | Message ID {message_id} | Telegram object {telegram_object}'.format(message_text=text, chat_id=chat_id, message_id=message_id, telegram_object=repr(telegram_message)))

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
