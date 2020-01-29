from telegram.ext import Updater, MessageHandler, Filters


bot_token = '938209950:AAGCa5apsW888s5K66rTjd7ePtorCCzRW3g'


def echo(update, context):
    msg = update.message
    context.bot.send_message(update.message.chat_id, msg.text)


def main():
    bot = Updater(bot_token, use_context=True)
    dp = bot.dispatcher

    dp.add_handler(MessageHandler(Filters.text, echo))

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
