import telebot

TOKEN = '8584163383:AAHnZprkPTPAJ3iDiGC8qQeHWB6W9sjPNeM'
bot = telebot.TeleBot(TOKEN)

user_lists = {}
user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in user_lists:
        user_lists[chat_id] = []

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add(
        telebot.types.KeyboardButton("Показать список"),
        telebot.types.KeyboardButton("Добавить элемент"),
        telebot.types.KeyboardButton("Удалить элемент"),
        telebot.types.KeyboardButton("Очистить список")
    )

    bot.send_message(chat_id, "Привет Давай создадим твой список", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in user_lists:
        user_lists[chat_id] = []

    if text == "Показать список":
        bot.send_message(chat_id, str(user_lists[chat_id]))

    elif text == "Добавить элемент":
        bot.send_message(chat_id, "Напиши элемент")
        user_state[chat_id] = "add"

    elif text == "Удалить элемент":
        bot.send_message(chat_id, "Напиши элемент")
        user_state[chat_id] = "remove"

    elif text == "Очистить список":
        user_lists[chat_id].clear()
        bot.send_message(chat_id, "Готово")

    elif chat_id in user_state:
        if user_state[chat_id] == "add":
            user_lists[chat_id].append(text)
            bot.send_message(chat_id, "Готово")

        elif user_state[chat_id] == "remove":
            if text in user_lists[chat_id]:
                user_lists[chat_id].remove(text)
            bot.send_message(chat_id, "Готово")

        user_state[chat_id] = None

    else:
        bot.send_message(chat_id, "Выбери действие")

bot.polling(none_stop=True)
