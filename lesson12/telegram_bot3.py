import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def hello(message):
    bot.send_message(message.chat.id, 'Hello')
    print('new message')


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
