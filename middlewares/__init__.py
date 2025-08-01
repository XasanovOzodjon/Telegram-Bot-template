# python-telegram-bot uchun bu faylda hech qanday kod kerak emas,
# chunki middleware tushunchasi mavjud emas.
# Agar throttling ishlatmoqchi bo‘lsangiz, handler funksiyalaringizga
# dekorator sifatida rate_limit ni qo‘llang.

# Masalan:
# from middlewares.throttling import rate_limit
#
# @rate_limit(2)
# def start(update, context):
#     update.message.reply_text("Salom!")

# Bu faylni bo‘sh qoldirishingiz mumkin.
