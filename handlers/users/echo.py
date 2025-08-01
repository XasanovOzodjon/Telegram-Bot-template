from telegram.ext import MessageHandler, Filters

def bot_echo(update, context):
    update.message.reply_text(update.message.text)

def register_handlers(dp):
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, bot_echo))