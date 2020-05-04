import requests
import bs4
import logging

from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext, CallbackQueryHandler

bot_token = '1104952265:AAF4AeLBahHy9bN4ukoYYp3YN9i01M3H8N8'
stockmarket_API_url = 'https://stockmarket.gov.ua/api/v1/feed-index.xml'
bot = Updater(bot_token, use_context=True)
dp = bot.dispatcher


def start(update, context: CallbackContext):
	msg = update.message
	context.bot.send_message(msg.chat_id, 'Пошук в базі НКЦПФР або новини комісії', reply_markup=ReplyKeyboardMarkup(
		[
			[KeyboardButton('Пошук в базі НКЦПФР')],
			[KeyboardButton('Новини НКЦПФР')]
		]
	))


def first_results(update, context):
	context.bot.send_message(update.message.chat_id, 'Введіть код ЄДР для пошуку: ')


def news(update, context):
	msg = update.message
	context.bot.send_message(msg.chat_id, 'Новини', reply_markup=InlineKeyboardMarkup(
		[
			[InlineKeyboardButton('Перейти на сайт НКЦПФР', url='https://www.nssmc.gov.ua/category/news/')]
		]
	))


def search(update, context):
	msg = update.message
	payload = {'edrpou': msg.text}
	r = requests.get(stockmarket_API_url, params=payload)
	soup = bs4.BeautifulSoup(r.text, 'xml')
	params = soup.find_all('param')
	if len(msg.text) == 8 and msg.text.isdigit():
		for param in params:
			if param.get('name') == 'D_NAME':
				name = param.text
				break
		try:
			context.bot.send_message(msg.chat_id, name)
			for link in soup.find_all('item'):
				report_url = link.get('href')
				timestamp = link.get('timestamp')

				if report_url.endswith('.txt'):
					context.bot.send_message(msg.chat_id, "Дата оприлюднення даних: " + timestamp[:10])
					context.bot.send_message(msg.chat_id, "Пряме посилання: " + report_url)
					context.bot.send_message(msg.chat_id, 'Текст звіту: ')
					report_url_deep = requests.get(report_url)

					report_url_deep_detali_txt = str(bs4.BeautifulSoup(report_url_deep.content, 'html.parser', ))
					parts_count = int(len(report_url_deep_detali_txt) / 4000)
					for i in range(parts_count):
						context.bot.send_message(msg.chat_id, report_url_deep_detali_txt[i: i + 4000])

				elif report_url.endswith('.xml'):
					context.bot.send_message(msg.chat_id, "Дата оприлюднення даних: " + timestamp[:10])
					context.bot.send_message(msg.chat_id, "Пряме посилання: " + report_url)
					context.bot.send_message(msg.chat_id, 'Текст звіту: ')
					report_url_deep = requests.get(report_url)
					report_url_deep_detali_xml = bs4.BeautifulSoup(report_url_deep.content, 'xml')
					for link in report_url_deep_detali_xml.find_all('z:row'):
						content = link.get('ZMIST')
						if content != None:
							parts_count = int(len(content) / 4000)
							for i in range(parts_count):
								context.bot.send_message(msg.chat_id, content[i: i + 4000])

		except NameError:
			context.bot.send_message(msg.chat_id, 'Запису не знайдено.')

	else:
		context.bot.send_message(msg.chat_id, 'Неправильний формат коду ЄДР. Спробуйте ще раз.')




def main():
	logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler(Filters.regex('Пошук в базі НКЦПФР'), first_results))
	dp.add_handler(MessageHandler(Filters.regex('Новини НКЦПФР'), news))
	dp.add_handler(MessageHandler(Filters.text, search))
	bot.start_polling()

if __name__ == '__main__':
	main()
