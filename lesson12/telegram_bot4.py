import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def hello(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)
    print('new message')


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
