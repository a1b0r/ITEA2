import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def check_for_admin(message):
    if message.text == 'admin':
        return True

@bot.message_handler(func=check_for_admin)
def hello(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)
    print('new message')


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
