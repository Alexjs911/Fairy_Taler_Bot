import telebot
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "What in the fuck do you want from me?")

@bot.message_handler(func=lambda msg:True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
