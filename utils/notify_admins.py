import logging
from data.config import ADMINS


def on_startup_notify(dp):
    for admin in ADMINS:
        try:
            dp.bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)
