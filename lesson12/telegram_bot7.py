import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(ommands=['start'])
def keyboard_example(message):
    bot.send_message(message.chat.id,'keyboard_example',reply_markup=message_kb)

    inline_kb = telebot.types.InlineKeyboardMarkup()
    buttons_list = []

    for i in range(21):
        buttons_list.append(telebot.types.InlineKeyboardButton(f'text_{i}',callback_data=str(i)))
    inline_kb.add(*buttons_list)
    bot.send_message(message.chat.id, 'inline_kb example', reply_markup=inline_kb)


@bot.callback_query_handler(func=lambda call: True)
def callback_example(call):
    print(call)


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
