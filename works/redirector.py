#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import telebot
import sys

token = '1166081834:AAEd4OVoJmRKSPJ4cBBpxb2sk4nBPMXpWlY'  # Вводим свой телеграм API токен
group_id = -1001184252611  # Вводим id группы, куда надо слать сообщения (обратите внимание, что id группы - отрицательное целое число)
bot = telebot.TeleBot(token, skip_pending=True)


# Ловим команду старта при старте без аргументов (первый старт)
@bot.message_handler(func=lambda message: True, commands=['start'])
def start(message):
    if len(sys.argv) != 1:
        return
    bot.send_message(message.chat.id, "ID чата: " + str(message.chat.id))
    print message.chat.id
    sys.exit()


# Если были переданы три аргумента, то возвращаем в чат сообщение
if len(sys.argv) == 4:
    callerid = str(sys.argv[1])
    exten = str(sys.argv[2])
    redirectnum = str(sys.argv[3])
    bot.send_message(group_id, "Вызов с номера " + callerid)
# Если аргумента нет, то считаем первым стартом и запускаем в режиме полинга
if len(sys.argv) == 1:
    bot.polling(none_stop=True)
