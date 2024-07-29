import telebot
from my_token import teleBot

# print(teleBot.TOKEN)
bot = telebot.TeleBot(token=teleBot.TOKEN)


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', )


# @bot.message_handler(commands=['info'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# content listed at my_token/message.py


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


bot.polling(none_stop=True)
# или # bot.infinity_polling()
