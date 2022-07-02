import telebot
import requests
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup
import Token


bot = telebot.TeleBot(Token.token_telegram)
print("start protgik")


@bot.message_handler(commands=['start'])
def start_message(finans):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Внести сумму в категорию")
	item2 = types.KeyboardButton("Статистика")

	markup.add(item1, item2)
	bot.send_message(finans.chat.id, "Здравствуйте! Что вы хотите сделать", reply_markup=markup)
	bot.register_next_step_handler(finans, еxamination_menu)

@bot.message_handler(commands=['help'])
def help_message(hel):
	bot.send_message(hel.chat.id, "help")


@bot.message_handler(content_types=['text'])
def еxamination_menu(finans):
	if finans.text == "Внести сумму в категорию":
		markup = types.ReplyKeyboardMarkup(row_width=1)
		item1 = types.KeyboardButton("Кар'єра")
		item2 = types.KeyboardButton("Сім'я")
		item3 = types.KeyboardButton("Оточення")
		item4 = types.KeyboardButton("Творчість і хоббі")
		item5 = types.KeyboardButton("Відпочинок та подорожі")
		item6 = types.KeyboardButton("Розвиток (освіта)")
		item7 = types.KeyboardButton("Здоров'я, спорт")
		markup.add(item1, item2, item3, item4, item5, item6, item7)

		bot.send_message(finans.chat.id, "Выберите категорию", reply_markup=markup)
		bot.register_next_step_handler(finans, еxamination_logics)

	elif finans.text == "Статистика":
		bot.register_next_step_handler(finans, statistics)


def еxamination_logics(finans):
	global category
	if finans.text == "Кар'єра":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Сім'я":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Оточення":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Творчість і хоббі":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Відпочинок та подорожі":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Розвиток (освіта)":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Здоров'я, спорт":
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)


def entry(finans):
	global sum_money
	bot.send_message(finans.chat.id, "Введите дату в формате 02.07.2022")
	sum_money = finans.text
	print(sum_money)
	bot.register_next_step_handler(finans, writing_to_file)

def writing_to_file(finans):
	global data, entry_list, fille
	data = finans.text
	print(data)
	a = 100
	entry_list = [category, sum_money]
	bot.send_message(finans.chat.id, "Все сохранено")
	if category == "Кар'єра":
		fille = open("Кар'єра.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")
	elif category == "Сім'я":
		fille = open("Сім'я.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")

	elif category == "Оточення":
		fille = open("Оточення.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")

	elif category == "Творчість і хоббі":
		fille = open("Творчість_і_хоббі.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")

	elif category == "Відпочинок та подорожі":
		fille = open("Відпочинок_та_подорожі.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")

	elif category == "Розвиток (освіта)":
		fille = open("Розвиток_(освіта).txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")

	elif category == "Здоров'я, спорт":
		fille = open("Здоров'я_спорт.txt","a")

		with fille as a:
			a.write(str(entry_list))
			a.write("\n")


def statistics(finans):
	try:
		bot.send_message(finans.chat.id, open("Кар'єра.txt"))
		bot.send_message(finans.chat.id, open("Сім'я.txt"))
		bot.send_message(finans.chat.id, open("Оточення.txt"))
		bot.send_message(finans.chat.id, open("Творчість_і_хоббі.txt"))
		bot.send_message(finans.chat.id, open("Відпочинок_та_подорожі.txt"))
		bot.send_message(finans.chat.id, open("Розвиток_(освіта).txt"))
		bot.send_message(finans.chat.id, open("Здоров'я_спорт.txt"))
	except FileNotFoundError:
		bot.send_message(finans.chat.id, "Запесей больше нет")



bot.polling(none_stop=True)
