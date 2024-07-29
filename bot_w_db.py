import telebot
import sqlite3
from data import keys


bot = telebot.TeleBot(token=keys.MY_TOKEN)
db = 'db.sqlite'
name = None


@bot.message_handler(commands=['start'])
def start(message):
    # CREATE CONNECTION TO DB
    conn = sqlite3.connect(db)  # actually db file creation if file doesn't exist
    # CREATE CURSOR FOR CURRENT CONNECTION
    cur = conn.cursor()
    # EXECUTE DB QUERY
    cur.execute('CREATE TABLE IF NOT EXISTS users '
                '(id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), pass VARCHAR(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Добро пожаловать в регистрацию! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    # global name
    password = message.text.strip()
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    # cur.execute(f'INSERT INTO users (name, pass) VALUES ("{name}", "{password}")')
    cur.execute("""INSERT INTO users(name, pass) VALUES(?, ?)""", (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for user in users:
        info += f'Имя: {user[1]}, пароль: {user[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
