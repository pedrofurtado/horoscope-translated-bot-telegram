import re
from flask import Flask, request
import telegram
import os
import asyncio
from utils import telegram_bot_url, telegram_bot_token, create_handlers

global bot
bot = telegram.Bot(token=telegram_bot_token())

app = Flask(__name__)

@app.route('/')
def home():
    return 'Horoscope Translated Bot Telegram - See more details in https://github.com/pedrofurtado/horoscope-translated-bot-telegram'

@app.route('/get_me')
def get_me():
    return str(bot.get_me())

@app.route('/setup_webhook', methods=['GET', 'POST'])
def setup_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=telegram_bot_url(), HOOK=telegram_bot_token()))

    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

async def bot_tele(text):
    application = (
        Application.builder().token(telegram_bot_token()).build()
    )

    create_handlers(application)

    await application.update_queue.put(Update.de_json(data=text, bot=application.bot))
    async with application:
        await application.start()
        await application.stop()

@app.route('/{}'.format(telegram_bot_token()), methods=['POST'])
def webhook():
    #update = telegram.Update.de_json(request.get_json(force=True), bot)
    #create_handlers(update.dispatcher)

    print("run with asyuncio")
    asyncio.run(bot_tele(request.get_json(force=True)))

    print("completed with asyuncio")

    return 'ok'

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
