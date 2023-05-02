from utils import create_updater, telegram_bot_token, telegram_bot_url_with_token
import os

updater = create_updater()

# App with only one route: POST /:bot_token
updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 3000)),
                      url_path=telegram_bot_token(),
                      webhook_url=telegram_bot_url_with_token()
                      )
