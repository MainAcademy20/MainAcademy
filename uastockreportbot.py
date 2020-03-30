import requests
import bs4

from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext, CallbackQueryHandler

bot_token = '1104952265:AAF4AeLBahHy9bN4ukoYYp3YN9i01M3H8N8'
stockmarket_API_url = 'https://stockmarket.gov.ua/api/v1/feed-index.xml'
bot = Updater(bot_token, use_context=True)
dp = bot.dispatcher

def start(update, context: CallbackContext):
	msg = update.message
	context.bot.send_message(msg.chat_id, 'Пошук в базі НКЦПФР або новири комісії', markup=ReplyKeyboardMarkup(
		[
			[KeyboardButton('Пошук в базі НКЦПФР')],
			[KeyboardButton('Новини НКЦПФР')]
		]
	))


def user_search(update, context):
	msg = update.message
	if msg.text.isdigit() and len(msg.text) == 8:
		return msg.text #context.bot.send_message(msg.chat_id, 'Ok....')
	else:
		return context.bot.send_message(msg.chat_id, 'Неправильний формат коду ЄДР. Спробуйте ще раз.')

def first_results(update, context):
	user_search(update, context)
	msg = update.message
	if msg.text == 'Пошук в базі НКЦПФР':
		context.bot.send_message(msg.chat_id, 'Введіть код ЄДР для пошуку: ')
	elif msg.text == 'Новини НКЦПФР':
		context.bot.send_message(msg.chat_id, reply_markup=InlineKeyboardMarkup(
			[
				[InlineKeyboardButton('Перейти на сайт НКЦПФР', url='https://www.nssmc.gov.ua/category/news/')]
			]
		))
def second_results():
	payload = {'edrpou': user_search()}
	r = requests.get(stockmarket_API_url, params=payload)
	soup = bs4.BeautifulSoup(r.text, 'xml')
	params = soup.find_all('param')
	for param in params:
		if param.get('name') == 'D_NAME':
			name = param.text
			break
	try:
		context.bot.send_message(msg.chat_id, name)
	except NameError:
		context.bot.send_message(msg.chat_id, 'Запису не знайдено.')

def main():
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler(Filters.text, first_results))
	dp.add_handler(MessageHandler(Filters.text, second_results))
	bot.start_polling()

if __name__ == '__main__':
	main()


