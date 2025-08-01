from telegram.ext import CommandHandler

def bot_help(update, context):
    text = (
        "Buyruqlar: ",
        "/start - Botni ishga tushirish",
        "/help - Yordam"
    )
    update.message.reply_text("\n".join(text))

def register_handlers(dp):
    dp.add_handler(CommandHandler("help", bot_help))