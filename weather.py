import telebot
import requests
import json
from data import keys

bot = telebot.TeleBot(token=keys.MY_TOKEN)
API = keys.MY_WEATHER_API_KEY


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши название города:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().replace(" ", "+")
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        # bot.reply_to(message, f'Сейчас погода: {res.json()}')  # выводит json объект
        data = json.loads(res.text)
        # print(data)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'data/sunny.png' if temp > 25 else 'data/clouds.png'
        bot.send_photo(message.chat.id, photo=open(image, 'rb'))
    else:
        bot.reply_to(message, 'Город не найден, попробуйте другой вариант ввода')


bot.polling(none_stop=True)
