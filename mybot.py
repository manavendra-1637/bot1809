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

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in config.list_buttons:
        keyboard.add(item)
    bot.send_message(message.chat_id, config.greetings, reply_markup=keyboard)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
    for item in config.list_answers:
        if message.text == item:
            bot.send_message(message.chat_id, item)

if __name__ == '__main__':
     bot.polling(none_stop=True)