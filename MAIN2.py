from telebot import types

wait_for_city = False

def start_module(bot, weather_forecast):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Введите язык')
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton('RU', callback_data='ru')
        b2 = types.InlineKeyboardButton('EN', callback_data='en')
        b3 = types.InlineKeyboardButton('FR', callback_data='fr')
        markup.row(b1, b2)
        markup.row(b3)

    @bot.message_handler(commands=['city'])
    def city(message):
        bot.send_message(message.chat.id, 'Введите свой город')
        global wait_for_city
        wait_for_city = True

    @bot.message_handler(content_types=['text'])
    def set_city(message):
        global wait_for_city
        if wait_for_city:
            if weather_forecast.set_city(message.text):
                bot.send_message(message.chat.id, f'Успешно установлен город {message.text}')
                wait_for_city = False
            else:
                bot.send_message(message.chat.id, 'Введите город еще раз')
        elif message == 'RU':
            weather_forecast.set_lang(message)
        elif message == 'EN':
            weather_forecast.set_lang(message)
        elif message == 'FR':
            weather_forecast.set_lang(message)
