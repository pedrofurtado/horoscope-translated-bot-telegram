import telegram.ext
import requests
import os

def telegram_bot_url():
  return os.getenv('TELEGRAM_BOT_URL')

def telegram_bot_url_with_token():
  return telegram_bot_url() + "/" + telegram_bot_token()

def telegram_bot_token():
  return os.getenv('TELEGRAM_BOT_TOKEN')

def get_daily_horoscope(sign, day):
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    data = response.json()["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'

    return horoscope_message

def start(update, context):
    update.message.reply_text("Hello! Welcome to Simplilearn1")

def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:

    /start -> Welcome to the channel
    /help -> This message
    /content -> Simplilearn offers various courses free of course through Skillup by Simplilearn
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information
     """)

def content(update, context):
    update.message.reply_text("We have various playlists and articles available!")

def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/Tm5u97I7OrM")

def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/pFq1pgli0OQ")

def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/i6AZdFxTK9I")

def Skillup(update, context):
    update.message.reply_text("tutorial link : https://www.simplilearn.com/?&utm_source=google&utm_medium=cpc&utm_term=%2Bwww%20%2Bsimplilearn%20%2Bcom&utm_content=803350713-40537012023-467574577661&utm_device=c&utm_campaign=Search-Brand-Broad-IN-AllDevice-adgroup-brand-navigation&gclid=Cj0KCQjw0oyYBhDGARIsAMZEuMv5mA9EysZZ5NfhK65Cb5OU0Q0TVC4con6DQzHF502-dfgA7QQFCgQaAu5sEALw_wcB")

def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")

def error(update, context):
    """Log Errors caused by Updates."""
    print('Update "%s" caused error "%s"', update, context.error)

def create_handlers(dispatcher):
  dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
  dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
  dispatcher.add_handler(telegram.ext.CommandHandler('content',content))
  dispatcher.add_handler(telegram.ext.CommandHandler('Python',Python))
  dispatcher.add_handler(telegram.ext.CommandHandler('SQL',SQL))
  dispatcher.add_handler(telegram.ext.CommandHandler('Java',Java))
  dispatcher.add_handler(telegram.ext.CommandHandler('Skillup',Skillup))
  dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact))
  dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
  dispatcher.add_error_handler(error)

def create_updater():
  updater = telegram.ext.Updater(telegram_bot_token(), use_context=True)
  disp = updater.dispatcher
  create_handlers(disp)
  return updater
