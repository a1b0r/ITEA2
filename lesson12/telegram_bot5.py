import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


#@bot.message_handler(func=lambda m: m.text == 'lambda')
@bot.message_handler(func=lambda m: m.chat.id not in admin_ids)
def hello(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)
    print('new message')


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
