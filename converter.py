import telebot
from telebot import types
from currency_converter import CurrencyConverter
from data import keys

bot = telebot.TeleBot(token=keys.MY_TOKEN)
cc = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введите сумму')
    bot.register_next_step_handler(message, _sum)


def _sum(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, повторите')
        bot.register_next_step_handler(message, _sum)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='OTHER')
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вводимая сумма должна быть больше нуля, повторите')
        bot.register_next_step_handler(message, _sum)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'OTHER':
        values = call.data.upper().split('/')
        res = cc.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Результат обмена: {round(res, 2)} {values[1]}, ожидаю новый ввод')
        bot.register_next_step_handler(call.message, _sum)
    else:
        bot.send_message(call.message.chat.id, 'Введите валютную пару через слэш "/"')
        bot.register_next_step_handler(call.message, _other)


def _other(message):
    try:
        values = message.text.upper().split('/')
        res = cc.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Результат обмена: {round(res, 2)} {values[1]}, ожидаю новый ввод')
        bot.register_next_step_handler(message, _sum)
    except Exception:
        bot.send_message(message.chat.id, f'Что то не так, ожидаю валютную пару через слэш "/"')
        bot.register_next_step_handler(message, _other)


bot.polling(none_stop=True)
