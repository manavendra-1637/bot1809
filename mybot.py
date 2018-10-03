# Name:        module1
# Purpose:
#
# Author:      MRulkevich
#
# Created:     20.09.2018
# Copyright:   (c) MRulkevich 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in config.list_buttons:
        keyboard.add(item)
    bot.send_message(message.chat.id, config.greetings, reply_markup=keyboard)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
    li = 0
    for item in config.list_buttons:
        bot.send_message(message.chat.id, str(li))
        if message.text == item:
            bot.send_message(message.chat.id, config.list_answers[li])
        li += 1

if __name__ == '__main__':
     bot.polling(none_stop=True)