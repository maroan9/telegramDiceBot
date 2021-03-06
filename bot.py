import logging
import os
from pathlib import Path

# Logs for debug
import coloredlogs
from dotenv import load_dotenv
from telegram import ParseMode
from telegram.ext import CommandHandler, Updater

from modules.dice import leerFormula

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# Load .env variables
env_file = Path('.env')
if env_file.is_file():
    load_dotenv(verbose=True)

# Load token form environment variables or code
token = os.getenv("TOKEN") if (os.getenv("TOKEN")) else 'TU TOKEN'


def hello(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))


def roll(bot, update, args):
    logger.warning(args)
    formula = args[0] if (len(args) != 0) else 'd6'
    tirar_dados = leerFormula(formula)
    bot.send_photo(chat_id=update.message.chat_id, photo=open('out.jpg', 'rb'))
    update.message.reply_text(
        text=tirar_dados,
        parse_mode=ParseMode.HTML
    )


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('roll', roll, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('r', roll, pass_args=True))


updater.start_polling()
updater.idle()
