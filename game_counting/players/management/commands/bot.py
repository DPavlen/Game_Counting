import os
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, TelegramError, Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater
from telegram.utils.request import Request
from dotenv import load_dotenv


from players.models import Player, Game, Payment, Team

# Теперь переменная TOKEN, описанная в файле .env,
load_dotenv()

TOKEN = os.getenv('TOKEN')
# updater = Updater(token=TOKEN)



def log_errors(f):
    """Декоратор отлова ошибок."""
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            raise e
    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text 

    reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        text = reply_text,
    )


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args: Any, **options: Any) -> str:
        """Вызов bot в manage.py."""
        # 1 - правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=TOKEN,
        )
        print(bot.get_me())
        
        # 2 - обработчики сообщений
        updater = Updater(
            bot=bot,
            use_context=True,
        ) 
        # MessageHandler реагирует на весь текст и если совпадает то идем в do_echo
        message_hadler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_hadler)

        # 3 - запустить бесконечную обработку взодящих сообщений
        updater.start_polling()
        updater.idle()
