from telegram import BotCommand


def set_default_commands(dp):
    dp.bot.set_my_commands(
        [
            BotCommand("start", "Botni ishga tushurish"),
            BotCommand("help", "Yordam"),
        ]
    )
