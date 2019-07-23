import telebot
import requests

bot = telebot.TeleBot("627705501:AAEvLXLycmen-FDNlsSbMlni5vWOdepQoY0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hey, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
