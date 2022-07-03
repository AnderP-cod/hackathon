import telebot
import re
import datetime
import requests
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup
import Token


bot = telebot.TeleBot(Token.token_telegram)
print("start protgik")


@bot.message_handler(commands=['start'])
def start_message(finans):
	bot.send_message(finans.chat.id, "Заповніть анкету")
	bot.send_message(finans.chat.id, "Як вас звати")
	bot.register_next_step_handler(finans, start_message_questionnaire)


def start_message_questionnaire(finans):
	global name
	name = finans.text
	print(name)
	bot.send_message(finans.chat.id, "Яка у вас дохід за тиждень")
	bot.register_next_step_handler(finans, start_message_questionnaire_many)


def start_message_questionnaire_many(finans):
	global many
	many = int(finans.text) 
	print(many)
	bot.send_message(finans.chat.id, f"Ім'я {name} Дохід {many}")
	bot.send_message(finans.chat.id, "Якщо ви записали щось не так то можете натиснути на star щоб спочатку заповнити анкету")
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Внести витрати до категорії")
	item2 = types.KeyboardButton("Статистика")

	markup.add(item1, item2)
	bot.send_message(finans.chat.id, "Доброго дня! Що ви хочете зробити", reply_markup=markup)
	bot.register_next_step_handler(finans, еxamination_menu)


@bot.message_handler(content_types=['text'])
def еxamination_menu(finans):
	if finans.text == "Внести витрати до категорії":
		markup = types.ReplyKeyboardMarkup(row_width=1)
		item1 = types.KeyboardButton("Кар'єра")
		item2 = types.KeyboardButton("Сім'я")
		item3 = types.KeyboardButton("Оточення")
		item4 = types.KeyboardButton("Творчість і хоббі")
		item5 = types.KeyboardButton("Відпочинок та подорожі")
		item6 = types.KeyboardButton("Розвиток (освіта)")
		item7 = types.KeyboardButton("Здоров'я, спорт")
		markup.add(item1, item2, item3, item4, item5, item6, item7)

		bot.send_message(finans.chat.id, "Оберіть категорію", reply_markup=markup)
		bot.register_next_step_handler(finans, еxamination_logics)

	elif finans.text == "Статистика":
		bot.send_message(finans.chat.id, "Натисніть 2 рази, щоб спрацювала кнопка")
		bot.register_next_step_handler(finans, statistics)


def еxamination_logics(finans):
	global category
	if finans.text == "Кар'єра":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Сім'я":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Оточення":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Творчість і хоббі":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Відпочинок та подорожі":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Розвиток (освіта)":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)

	elif finans.text == "Здоров'я, спорт":
		bot.send_message(finans.chat.id, "Введіть суму грошей скільки ви витратили")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)


def entry(finans):
	global sum_money
	print(f"{many} анкета")
	bot.send_message(finans.chat.id, "Введіть сьогоднішню дату у форматі 2022-07-03\n1)(yyyy-mm-dd)\n2)(- тере теж обов'язково))")
	sum_money = int(finans.text)
	if sum_money <= many:
		print(sum_money)
		bot.register_next_step_handler(finans, writing_to_file)
		print(datetime.date.today())
	elif sum_money > many:
		bot.send_message(finans.chat.id, "Ви ввели більше, ніж ви вказали в анкеті")


def writing_to_file(finans):
	global data, entry_list, fille, json_fille
	data = finans.text
	now = datetime.date.today()
	try:
		if data == str(now):
			print(data)
			sum_money_2 = [int(sum_money)]
			bot.send_message(finans.chat.id, "Все збережено")
		else:
			bot.send_message(finans.chat.id, "Ви ввели не сьогоднішню дату")
	except Exception:
		bot.send_message(finans.chat.id, "Ви ввели не сьогоднішню дату")

	if category == "Кар'єра":
		fille = open("Кар'єра.txt", "a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Сім'я":
		fille = open("Сім'я.txt", "a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Оточення":
		fille = open("Оточення.txt","a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Творчість і хоббі":
		fille = open("Творчість і хоббі.txt","a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Відпочинок та подорожі":
		fille = open("Відпочинок та подорожі.txt","a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Розвиток (освіта)":
		fille = open("Розвиток (освіта).txt", "a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Здоров'я, спорт":
		fille = open("Здоров'я, спорт.txt","a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()


def statistics(finans):
	try:
		bot.send_message(finans.chat.id, "Кар'єра")
		with open("Кар'єра.txt", 'r') as f:
			a = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if a == 9:
				bot.send_message(finans.chat.id, f"{a}% Норма")
			elif a > 9:
				bot.send_message(finans.chat.id, f"{a}% Ви перевищили норму")
			elif a < 9:
				bot.send_message(finans.chat.id, f"{a}% Ви принизили норму")
		
		bot.send_message(finans.chat.id, "Сім'я")
		with open("Сім'я.txt", 'r') as f:
			s = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if s == 30:
				bot.send_message(finans.chat.id, f"{s}% Норма")
			elif s > 30:
				bot.send_message(finans.chat.id, f"{s}% Ви перевищили норму")
			elif s < 30:
				bot.send_message(finans.chat.id, f"{s}% Ви принизили норму")

		bot.send_message(finans.chat.id, "Оточення")
		with open("Оточення.txt", 'r') as f:
			d = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if d == 5:
				bot.send_message(finans.chat.id, f"{d}% Норма")
			elif d > 5:
				bot.send_message(finans.chat.id, f"{d}% Ви перевищили норму")
			elif d < 5:
				bot.send_message(finans.chat.id, f"{d}% Ви принизили норму")

		bot.send_message(finans.chat.id, "Творчість і хоббі")
		with open("Творчість і хоббі.txt", 'r') as f:
			f = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if f == 10:
				bot.send_message(finans.chat.id, f"{f}% Норма")
			elif f > 10:
				bot.send_message(finans.chat.id, f"{f}% Ви перевищили норму")
			elif f < 10:
				bot.send_message(finans.chat.id, f"{f}% Ви принизили норму")

		bot.send_message(finans.chat.id, "Відпочинок та подорожі")
		with open("Відпочинок та подорожі.txt", 'r') as f:
			g = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if g == 14:
				bot.send_message(finans.chat.id, f"{g}% Норма")
			elif g > 14:
				bot.send_message(finans.chat.id, f"{g}% Ви перевищили норму")
			elif g < 14:
				bot.send_message(finans.chat.id, f"{g}% Ви принизили норму")
			
		bot.send_message(finans.chat.id, "Розвиток (освіта)")
		with open("Розвиток (освіта).txt", 'r') as f:
			h = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if h == 15:
				bot.send_message(finans.chat.id, f"{h}% Норма")
			elif h > 15:
				bot.send_message(finans.chat.id, f"{h}% Ви перевищили норму")
			elif h < 15:
				bot.send_message(finans.chat.id, f"{h}% Ви принизили норму")

		bot.send_message(finans.chat.id, "Здоров'я, спорт")
		with open("Здоров'я, спорт.txt", 'r') as f:
			j = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if j == 17:
				bot.send_message(finans.chat.id, f"{j}% Норма")
			elif j > 17:
				bot.send_message(finans.chat.id, f"{j}% Ви перевищили норму")
			elif j < 17:
				bot.send_message(finans.chat.id, f"{j}% Ви принизили норму")
	except FileNotFoundError:
		bot.send_message(finans.chat.id, "Записів більше немає")


bot.polling(none_stop=True)
