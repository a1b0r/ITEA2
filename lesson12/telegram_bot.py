import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    print(message)
    print('new message')


if __name__ == '__main__':
    bot.polling()