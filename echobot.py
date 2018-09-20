#-------------------------------------------------------------------------------
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

if __name__ == '__main__':
     bot.polling(none_stop=True)