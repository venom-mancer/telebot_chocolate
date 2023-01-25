import  telebot
import os
import requests
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import random

API_KEY = 'mykey'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = 'yo yo Nig'
    bot.send_message(message.chat.id, msg) 


@bot.message_handler(func=lambda m: True)
def repeat(message):

    luck = random.randint(1, 5)
    uid = message.chat.username
    
    if '@big_black_chocolate_bot' in message.text :
        result = [ t for t in message.text.split() if t.startswith('@') ]
        reply = bot.send_message(message.chat.id, 'WP')
        print(reply)

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()

