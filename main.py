import telebot
from telebot import types
from mym import WeatherForecast
from MAIN2 import start_module
import schedule
from threading import Thread

token = '5134305679:AAHQcl-BUQ0TOadGJVTP6UgGYb3hCJO8cFQ'
bot = telebot.TeleBot(token)
weather_forecast = WeatherForecast()
chat_id = None

bot.set_my_commands([types.BotCommand('start', 'старт'), types.BotCommand('schedule', 'не знаю')])

start_module(bot, weather_forecast)

@bot.message_handler(commands=['schedule'])
def schedule_hello(message):
    global chat_id
    chat_id = message.chat.id

def send_hello():
    if chat_id is not None:
        bot.send_message(chat_id, 'Hello')

def schedule_checker():
    while True:
        schedule.run_pending()

schedule.every(10).seconds.do(send_hello)
Thread(target=schedule_checker).start()

bot.infinity_polling()