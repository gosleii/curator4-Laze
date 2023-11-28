import telebot
bot = telebot.TeleBot('6407787392:AAFjaIFk1nQyQ3VxUIpXxco3GQbuToiGEuE')


@bot.message_handler(commands=['start'])
def main(message): bot.send_message(message.chat.id, 'привет')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'бегиии')

bot.infinity_polling()