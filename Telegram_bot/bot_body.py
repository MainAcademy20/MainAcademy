import requests
from time import gmtime , strftime
from telegram.ext import Updater, MessageHandler, Filters


bot_token = '1016011895:AAHKtvxJzuiG78qiviC2Kuzxct70WGjDIDM'
PRIVAT_EXCHANGE_API_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


def human_readable_ccy(ccy_obj):
	# USD-UAH: 24.15000/24.55000
	return "{}-{}: {}/{}".format(
		ccy_obj['ccy'], ccy_obj['base_ccy'], ccy_obj['buy'], ccy_obj['sale'])


def echo(update, context):
	msg = update.message
	response = requests.get(PRIVAT_EXCHANGE_API_URL)
	time_now = strftime('%d/%m/%Y  %H:%M:%S')
	# [{"ccy":"USD","base_ccy":"UAH","buy":"24.15000","sale":"24.55000"}, ...]
	list_ccy = response.json()
	list_ccy_human = list(map(human_readable_ccy, list_ccy))


	context.bot.send_message(msg.chat_id, 'Курс валют по состоянию на : ' + '\n' +
						time_now +	'\n' +  '\n' + '\n'.join(list_ccy_human))


def main():
	bot = Updater(bot_token, use_context=True)
	dp = bot.dispatcher

	dp.add_handler(MessageHandler(Filters.text, echo))

	bot.start_polling()



if __name__ == '__main__':
	main()