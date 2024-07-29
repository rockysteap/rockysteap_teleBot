import telebot
from telebot import types
import webbrowser

from data import keys

# print(keys.TOKEN)
bot = telebot.TeleBot(token=keys.MY_TOKEN)
MY_URL = keys.MY_URL


# CONTENT HANDLER (example with photo)
@bot.message_handler(content_types=['photo'])  # =['photo', 'audio', 'video']
def get_photo(message):
    # BUTTONS CREATOR
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url=MY_URL)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    # markup.add(btn1, btn2, btn3)
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Красивое фото!', reply_markup=markup)


# BUTTONS HANDLER
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', chat_id=callback.message.chat.id, message_id=callback.message.message_id)


# COMMANDS HANDLER
@bot.message_handler(commands=['site', 'web', 'website'])
def site(message):
    webbrowser.open_new_tab(url=MY_URL)


# @bot.message_handler(commands=['info'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# content listed at my_token/message.py

@bot.message_handler(commands=['main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', )


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn1)
    markup.row(btn2, btn3)
    file = open('data/photo.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is opened')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


# TEXT HANDLER (goes after command handlers or will handle commands as well)
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', )
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    #     Another option - to handle commands inside method, like this:
    #     elif message.text.lower() == '/start':


# INFINITY RUN LOOP
bot.polling(none_stop=True)
# или # bot.infinity_polling()
