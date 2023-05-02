# Horoscope Translated Bot Telegram

## Demo

https://horoscope-translated-bot-telegram.vercel.app

## Running Locally

```bash
docker container run --rm -it --name horoscope-translated-bot-telegram -w /srv -v $(pwd):/srv -p 3000:3000 python:3.7 /bin/bash
  > python -m venv venv/
  > source venv/bin/activate
  > pip install -r requirements.txt
  > TELEGRAM_BOT_URL=https://horoscope-translated-bot-telegram.vercel.app TELEGRAM_BOT_TOKEN=bot-token flask --app bot/webhook run --port 3000 --host 0.0.0.0 --debug
  > TELEGRAM_BOT_URL=https://horoscope-translated-bot-telegram.vercel.app TELEGRAM_BOT_TOKEN=bot-token python bot/polling.py
```

Your Flask application is now available at `http://localhost:3000`.
