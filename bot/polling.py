from utils import create_updater

updater = create_updater()
updater.start_polling()
updater.idle()
