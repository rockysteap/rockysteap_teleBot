import telebot
import webbrowser
from my_token import teleBot

# print(teleBot.TOKEN)
bot = telebot.TeleBot(token=teleBot.TOKEN)

@bot.message_handler(commands=['site', 'web', 'website'])
def site(message):
    webbrowser.open_new_tab('https://artschool.pythonanywhere.com/')

# @bot.message_handler(commands=['info'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# content listed at my_token/message.py

# COMMAND HANDLER
@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', )


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
