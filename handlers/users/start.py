from telegram.ext import CommandHandler

def bot_start(update, context):
    update.message.reply_text(f"Salom, {update.effective_user.full_name}!")

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", bot_start))