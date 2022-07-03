import telebot
import json
import re
import time
import requests
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup
import Token


bot = telebot.TeleBot(Token.token_telegram)
print("start protgik")


@bot.message_handler(commands=['start'])
def start_message(finans):
	bot.send_message(finans.chat.id, "Заполните анкету")
	bot.send_message(finans.chat.id, "Как вас завут")
	bot.register_next_step_handler(finans, start_message_questionnaire)


def start_message_questionnaire(finans):
	global name
	name = finans.text
	print(name)
	bot.send_message(finans.chat.id, "Какая у вас зарплата в неделю")
	bot.register_next_step_handler(finans, start_message_questionnaire_many)


def start_message_questionnaire_many(finans):
	global many
	many = int(finans.text) 
	print(many)
	bot.send_message(finans.chat.id, f"Имя {name} Зарплата {many}")
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
		bot.send_message(finans.chat.id, "Введите сумму денег сколько вы потратели в грн")
		category = finans.text
		print(category)
		bot.register_next_step_handler(finans, entry)


def entry(finans):
	global sum_money
	print(f"{many} анкета")
	bot.send_message(finans.chat.id, "Введите сегоднишнюю дату в формате 07/02/2022 (/ слеш тоже обязател))")
	sum_money = int(finans.text)
	try:
		if sum_money <= many:
			print(sum_money)
			bot.register_next_step_handler(finans, writing_to_file)
		elif sum_money > many:
			bot.send_message(finans.chat.id, "Вы ввели больше чем вы указали в анкете")
	except Exception:
		bot.send_message(finans.chat.id, "Ошибка нажмите на start или на пишите")

def writing_to_file(finans):
	global data, entry_list, fille, json_fille
	data = finans.text
	try:
		valid_date = time.strptime(data, '%m/%d/%Y')
		print(data)
		sum_money_2 = [int(sum_money)]
		bot.send_message(finans.chat.id, "Все сохранено")
	except ValueError:
		bot.send_message(finans.chat.id, "Выввели не сегоднишную дату")

	except Exception:
		bot.send_message(finans.chat.id, "Выввели не сегоднишную дату")

	if category == "Кар'єра":
		fille = open("Кар'єра.txt","a")
		fille_txt = {'category': category, 'money': sum_money_2}
		fille.write(str(fille_txt))
		fille.close()

	elif category == "Сім'я":
		fille = open("Сім'я.txt","a")
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
		fille = open("Розвиток (освіта).txt","a")
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
				bot.send_message(finans.chat.id, f"{a}% Вы перевышели норму")
			elif a < 9:
				bot.send_message(finans.chat.id, f"{a}% Вы принизели норму")
		
		bot.send_message(finans.chat.id, "Сім'я")
		with open("Сім'я.txt", 'r') as f:
			s = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if s == 30:
				bot.send_message(finans.chat.id, f"{s}%")
			elif s > 30:
				bot.send_message(finans.chat.id, f"{s}% Вы перевышели норму")
			elif s < 30:
				bot.send_message(finans.chat.id, f"{s}% Вы принизели норму")

		bot.send_message(finans.chat.id, "Оточення")
		with open("Оточення.txt", 'r') as f:
			d = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if d == 5:
				bot.send_message(finans.chat.id, f"{d}%")
			elif d > 5:
				bot.send_message(finans.chat.id, f"{d}% Вы перевышели норму")
			elif d < 5:
				bot.send_message(finans.chat.id, f"{d}% Вы принизели норму")

		bot.send_message(finans.chat.id, "Творчість і хоббі")
		with open("Творчість і хоббі.txt", 'r') as f:
			f = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if f == 10:
				bot.send_message(finans.chat.id, f"{f}%")
			elif f > 10:
				bot.send_message(finans.chat.id, f"{f}% Вы перевышели норму")
			elif f < 10:
				bot.send_message(finans.chat.id, f"{f}% Вы принизели норму")

		bot.send_message(finans.chat.id, "Відпочинок та подорожі")
		with open("Відпочинок та подорожі.txt", 'r') as f:
			g = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if g == 14:
				bot.send_message(finans.chat.id, f"{g}%")
			elif g > 14:
				bot.send_message(finans.chat.id, f"{g}% Вы перевышели норму")
			elif g < 14:
				bot.send_message(finans.chat.id, f"{g}% Вы принизели норму")
			
		bot.send_message(finans.chat.id, "Розвиток (освіта)")
		with open("Розвиток (освіта).txt", 'r') as f:
			h = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if h == 15:
				bot.send_message(finans.chat.id, f"{h}%")
			elif h > 15:
				bot.send_message(finans.chat.id, f"{h}% Вы перевышели норму")
			elif h < 15:
				bot.send_message(finans.chat.id, f"{h}% Вы принизели норму")

		bot.send_message(finans.chat.id, "Здоров'я, спорт")
		with open("Здоров'я, спорт.txt", 'r') as f:
			j = sum(map(int, re.findall(r'-?\d+', f.read())))//100
			if j == 17:
				bot.send_message(finans.chat.id, f"{j}%")
			elif j > 17:
				bot.send_message(finans.chat.id, f"{j}% Вы перевышели норму")
			elif j < 17:
				bot.send_message(finans.chat.id, f"{j}% Вы принизели норму")
	except FileNotFoundError:
		bot.send_message(finans.chat.id, "Запесей больше нет")


bot.polling(none_stop=True)
