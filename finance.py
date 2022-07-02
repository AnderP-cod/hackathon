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
	bot.register_next_step_handler(finans, еxamination)

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
		bot.send_message(finans.chat.id, "(Статистика)")
		bot.register_next_step_handler(finans, statistics)


def еxamination_logics(finans):
	if finans.text == "Кар'єра"
		pass

	elif finans.text == "Кар'єра"
		pass


def statistics(finans):
	pass


bot.polling(none_stop=True)
