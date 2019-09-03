import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(ommands=['start'])
def keyboard_example(message):
    message_kb = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=3)

    message_kb.row('1','2','3')
    message_kb.row('4','5','6')
    bot.send_message(message.chat.id,'keyboard_example',reply_markup=message_kb)


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
