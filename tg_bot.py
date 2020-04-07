from telegram import Update
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters
from dataforbot import PRIVAT_EXCHANGE_API_URL, bot_token
from settings_reading_writing import *

from datetime import datetime
import requests
from log_reading import count_event, logs_reading

keyboard = [['/time', '/moneychange'],
            ['/settings','/logs'],
			['/graphic report']
		   ]




keyboard_In = [  [InlineKeyboardButton("/toRead")] ,
			   	 [InlineKeyboardButton("/Update")]
			  ]
# IKM = InlineKeyboardMarkup(keyboard_In)


RKM = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True,
    one_time_keyboard=True
)




def human_readable_ccy(ccy_obj):
	# USD-UAH: 24.15000/24.55000
	return "{}-{}: {}/{}".format(
		ccy_obj['ccy'], ccy_obj['base_ccy'], ccy_obj['buy'], ccy_obj['sale'])


def get_time(update: Update, context: CallbackContext):
	time_now = datetime.now()
	str_time = data_time_decor(time_now)
	context.bot.send_message(chat_id=update.message.chat_id, text=str_time, reply_markup=RKM)


def data_time_decor(time_now):
	msg_datatime = time_now.strftime('date : \n%Y-%m-%d \ntime :\n%H:%M:%S')
	return msg_datatime


def print_exchange(update: Update, context: CallbackContext):
	response = requests.get(PRIVAT_EXCHANGE_API_URL)
	list_ccy = response.json()
	human_ccy = '\n'.join(list(map(human_readable_ccy, list_ccy)))
	context.bot.send_message(chat_id=update.message.chat_id, text=human_ccy, reply_markup=RKM)


def print_logs(update: Update, context: CallbackContext):
	logs_for_print =  count_event(logs_reading())

	warning= 'Кол-во WARNING = {}'.format(logs_for_print[0])
	unnorm= 'Кол-во UnNORM = {}'.format(logs_for_print[1])
	error = 'Кол-во ERROR = {}'.format(logs_for_print[2])
	message_log ="{}\n{}\n{}\n".format(warning, unnorm, error)
	context.bot.send_message(chat_id=update.message.chat_id, text=message_log, reply_markup=RKM)


def settings(update: Update, context: CallbackContext):
	""" Импорт данных с settings_reading_writing.py"""

	t = ('\n'+ t01 +'\n'+ t23 +'\n'+ t45 +'\n'+ t67 +'\n'+ t89 +'\n'+ t1011 +'\n'+ t1213 +'\n'+ t1415)
	msg = update.message.text                                            # t01, t23, t45, t67, t89, t1011, t1213, t1415


	""" НЕ красивое использование контекст бота"""
	context.bot.send_message(chat_id=update.message.chat_id, text=msg , reply_markup=RKM)
	# context.bot.send_message(chat_id=update.message.chat_id, reply_markup=RKM)
	context.bot.send_message(chat_id=update.message.chat_id, text=t, reply_markup=InlineKeyboardMarkup
		([
		 [InlineKeyboardButton("/toRead", callback_data='toRead'),
		 InlineKeyboardButton("/Update", callback_data='Update')]
	     ])
	)


def echo(update, context):
	# msg = update.message
	# response_privat = requests.get(PRIVAT_EXCHANGE_API_URL)
	# #[{"ccy":"USD","base_ccy":"UAH","buy":"24.15000","sale":"24.55000"}, ...]
	# list_ccy_privat = response_privat.json()
	# list_ccy_human = list(map(human_readable_ccy, list_ccy_privat))
	# now_datetime = datetime.now()

	# context.bot.send_message(msg.chat_id, '\n'.join(list_ccy_human))
	# context.bot.send_message(chat_id=update.message.chat_id, text='hello')
	text = update.message.text  # Получаем текст того, что нам написали
	context.bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=RKM)





def main():
	# Создаем bot как экземпляр класса Updater

	bot = Updater(bot_token, use_context=True)

	setting_handler = CommandHandler('settings', settings)
	bot.dispatcher.add_handler(setting_handler)

	logs_handler = CommandHandler('logs', print_logs)
	bot.dispatcher.add_handler(logs_handler)

	change_handler = CommandHandler('moneychange', print_exchange)
	bot.dispatcher.add_handler(change_handler)

	time_handler = CommandHandler('time', get_time)
	bot.dispatcher.add_handler(time_handler)

	dp = bot.dispatcher
	dp.add_handler(MessageHandler(Filters.text, echo))

	bot.start_polling()
	# bot.idle()  ????????????????

if __name__ == '__main__':
	main()