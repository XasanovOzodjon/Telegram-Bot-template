import logging
from telegram.error import (
    Unauthorized, TelegramError,
    BadRequest, RetryAfter
)
from telegram.ext import Dispatcher, CallbackContext
from telegram import Update

def error_handler(update: Update, context: CallbackContext):
    try:
        raise context.error
    except Unauthorized as e:
        logging.exception(f'Unauthorized: {e}')
    except BadRequest as e:
        logging.exception(f'BadRequest: {e}')
    # except InvalidQueryID as e:
    #     logging.exception(f'InvalidQueryID: {e} \nUpdate: {update}')
    except RetryAfter as e:
        logging.exception(f'RetryAfter: {e} \nUpdate: {update}')
    except TelegramError as e:
        logging.exception(f'TelegramError: {e} \nUpdate: {update}')
    except Exception as e:
        logging.exception(f'Update: {update} \n{e}')

# Ushbu handlerni dispatcherga ro'yxatdan o'tkazish kerak:
# dp.add_error_handler(error_handler)
