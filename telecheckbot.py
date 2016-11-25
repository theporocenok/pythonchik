#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

token = "";
bot = telebot.TeleBot(token)

chats = [297617298]

def TakeTextFrom(file):
	f = open(str(file))
	textFROMstatustxt = f.read()
	f.close()
	return textFROMstatustxt

@bot.message_handler(commands=['status'])
def send_welcome(message):
	if not message.chat.id in chats:
		msg = bot.send_message(message.chat.id, 'Дармаму, ты пришёл договориться?')
		return 0

	try:
		textFROMstatus=str(TakeTextFrom("Ahtarova.txt"))
		textFROMstatus+=str(TakeTextFrom("Ershova.txt"))
		textFROMstatus+=str(TakeTextFrom("Gluhova.txt"))
		textFROMstatus+=str(TakeTextFrom("Samsonova.txt"))
		textFROMstatus+=str(TakeTextFrom("Zinnatshina.txt"))
		msg = bot.send_message(message.chat.id, textFROMstatus)
	except IOError:
		msg = bot.send_message(message.chat.id, 'status.txt not found')

@bot.message_handler(commands=['getid'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, message.chat.id)

if __name__ == '__main__':
	bot.polling(none_stop=True)
