import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

# Logs for debug
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# Load .env variables
load_dotenv(verbose=True)
token = os.getenv("TOKEN")


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
