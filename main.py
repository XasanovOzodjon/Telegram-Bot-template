from telegram.ext import Updater
from loader import bot
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def main():
    updater = Updater(bot.token, use_context=True)
    dp = updater.dispatcher

    set_default_commands(dp)
    on_startup_notify(dp)

    handlers.register_handlers(dp)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
