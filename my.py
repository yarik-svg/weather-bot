import telebot
from setting import token
from bot_logik import *
bot=telebot.Telebot(token)
@bot.message_handler(commands=['start'])
def sent_start(message):
    bot.send_message(message.chat.id,"привет бот прогноз погоды")
@bot.message_handler(commands=["weather"])
def weather(message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, укажи город. Пример: /weather Madrid"
        )
        return

    city = parts[1]

    weather_info = get_weather(city)

    bot.send_message(
        message.chat.id,
        f"Погода в {city}: {weather_info}"
    )
    speak(weather_info)

# Запуск бота
bot.polling()
