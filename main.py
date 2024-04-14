from telebot import *
import sqlite3
bot = TeleBot('6393211561:AAE1s8qXXq8wOzL3eSV5l03dlv-xei-Ll3I')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('i_zaibalsa.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id,'ща быренько тебя зарегаем и на СВО , введите ваш ник')
    bot.register_next_step_handler(message,user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('i_zaibalsa.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name,pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    ab = types.InlineKeyboardMarkup()
    ab.add(types.InlineKeyboardButton('Список пользователей', callback_data='users_table_function'))
    bot.send_message(message.chat.id, 'Вы зарегались',reply_markup=ab)


@bot.callback_query_handler(func=lambda call: True)
def users_table_function(call):
    conn = sqlite3.connect('i_zaibalsa.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    table = cur.fetchall()
    info = ''
    for i in table:
        info += f'Имя: {i[1]},пароль:{i[2]}\n'

    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)














@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'милашка')


@bot.message_handler(commands=['start'])
def start(message):
    file = open('./xer.jpg','rb')
    bot.send_photo(message.chat.id,file)
    a = types.ReplyKeyboardMarkup()
    a.add(types.KeyboardButton("Перейти "))
    a.add(types.KeyboardButton('Удалить сообщение'))
    bot.send_message(message.chat.id, f'Дарова,{message.from_user.first_name}  Нажмите на кнопку  Перейти   чтобы перейти на график биткоина',reply_markup=a)
    bot.register_next_step_handler(message,on_click)

def on_click(message):
    if message.text == 'Перейти':
        bot.send_message(message.chat.id,'вот ссылка на график битка:  https://ru.tradingview.com/symbols/BTCUSD/')
    elif message.text == 'Удалить сообщение':
        bot.send_message(message.chat.id, 'блять ,не работает ')




@bot.message_handler(commands=['site'])
def site(message):
    a = types.InlineKeyboardMarkup()
    a.add(types.InlineKeyboardButton("Перейти ", url='https://ru.tradingview.com/symbols/BTCUSD/'))
    a.add(types.InlineKeyboardButton('Удалить сообщение', callback_data='delete'))
    a.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Нажать" чтобы перейти на график биткоина , что бы удалить сообщение нажмите на "Удалить сообщение",'
    ' также есть Edit ==> "Изменить текст"', reply_markup=a)

@bot.callback_query_handler(func=lambda callback: True)
def callback_m(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Obeme черножопый', callback.message.chat.id, callback.message.message_id)






@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Ti dayn!")


#@bot.message_handler(commands=['start'])
#def start(message):
    #bot.send_message(message.chat.id, f'Дарова,{message.from_user.first_name}')


@bot.message_handler(commands=['ability'])
def ability(message):
    bot.send_message(message.chat.id, "я могу отправлять тебе графики крипотовалют")



bot.infinity_polling()
