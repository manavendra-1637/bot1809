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
import requests, bs4

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in config.list_buttons:
        keyboard.add(item)
    bot.send_message(message.chat.id, config.greetings, reply_markup=keyboard)

@bot.message_handler(commands=['news'])
def getnews(message):
   adrsite = "https://www.newsvl.ru"
   site = requests.get(adrsite)
   parse = bs4.BeautifulSoup(site.text, "html.parser")
   tmp1 = parse.select('.page__content_important .page__main-story-container .page__main-story .story-list .story-list__item-title')
   strnews = str(tmp1[0])
   start = strnews.find('a href') + 8
   end = strnews.find('>', start) - 1

   news = tmp1[0].getText() + ' ' + adrsite + strnews[start:end]
   bot.send_message(message.chat.id, news)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
    li = 0
    found = False
    for item in config.list_buttons:
        if message.text == item:
            bot.send_message(message.chat.id, config.list_answers[li])
            found = True
        li += 1

    if not found:
       bot.send_message(config.muid, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)