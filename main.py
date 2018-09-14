#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MRulkevich
#
# Created:     14.09.2018
# Copyright:   (c) MRulkevich 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-*- coding: utf-8 -*-
import telebot

token = '450119806:AAE4IcyaqMdltbZZCFIEpYKYTTKGBBBBgek'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all(message):
    bot.send_message(message.chat_id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)