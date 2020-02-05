import requests
from telegram.ext import Updater, MessageHandler, Filters
from datetime import datetime

bot_token = '938209950:AAGCa5apsW888s5K66rTjd7ePtorCCzRW3g'
PRIVAT_EXCHANGE_API_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
now = datetime.now().strftime('%a %d %B %Y, %H:%M:%S')


def human_readable_ccy(ccy_obj):
    # USD-UAH: 24.15000/24.55000
    return "{}-{}: {}/{}".format(
        ccy_obj['ccy'], ccy_obj['base_ccy'], ccy_obj['buy'], ccy_obj['sale'])


def echo(update, context):
    msg = update.message
    response = requests.get(PRIVAT_EXCHANGE_API_URL)
    # [{"ccy":"USD","base_ccy":"UAH","buy":"24.15000","sale":"24.55000"}, ...]
    list_ccy = response.json()
    list_ccy_human = list(map(human_readable_ccy, list_ccy))

    context.bot.send_message(msg.chat_id, '\n'.join(list_ccy_human))
    context.bot.send_message(msg.chat_id, now)


def main():
    bot = Updater(bot_token, use_context=True)
    dp = bot.dispatcher

    dp.add_handler(MessageHandler(Filters.text, echo))

    bot.start_polling()


if __name__ == '__main__':
    main()
