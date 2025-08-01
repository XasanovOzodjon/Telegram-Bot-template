import time
from functools import wraps
from telegram import Update
from telegram.ext import CallbackContext

# Oddiy throttling uchun global dict
_user_last_time = {}

def rate_limit(limit: int):
    def decorator(func):
        @wraps(func)
        def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
            user_id = update.effective_user.id
            now = time.time()
            last_time = _user_last_time.get(user_id, 0)
            if now - last_time < limit:
                update.message.reply_text("Too many requests!")
                return
            _user_last_time[user_id] = now
            return func(update, context, *args, **kwargs)
        return wrapper
    return decorator

# python-telegram-bot uchun middleware klassi kerak emas.
# Faqat yuqoridagi dekoratordan foydalaning va handler funksiyalaringizga qo'llang.