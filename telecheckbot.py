#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import sys
sys.path.insert(0, '/home/pi/py')

import config

token = config.tele_token;
bot = telebot.TeleBot(token)

chats = [297617298]
dir='/home/pi/py/brut/status/'

def TakeTextFrom(*files):
	textFROMstatustxt=''
	print(str(files))
	for file in files:
		print(file)
		f = open(str(file))
		textFROMstatustxt += f.read()
		f.close()
	return textFROMstatustxt

@bot.message_handler(commands=['status'])
def send_welcome(message):
	if not message.chat.id in chats:
		msg = bot.send_message(message.chat.id, 'Дормамму, ты пришёл договориться?')
		return 0

	try:
		textFROMstatus=str(TakeTextFrom(dir+'Ahtarova.txt',dir+'Ershova.txt',dir+'Gluhova.txt',dir+'Samsonova.txt',dir+'Zinnatshina.txt'))
		msg = bot.send_message(message.chat.id, textFROMstatus)
	except IOError:
		msg = bot.send_message(message.chat.id, 'Не знаю о чём ты, Дормамму, никаких статусов я не нашёл!')

@bot.message_handler(commands=['getid'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, message.chat.id)

if __name__ == '__main__':
	bot.polling(none_stop=True)
