import  telebot
import os
import requests

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = 'yo yo Nig'
    bot.send_message(message.chat.id, msg) 


@bot.message_handler(func=lambda m: True)
def repeat(message):
    message.from_user.username
    bot.send_message(message.from_user.username, message.text)

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()

