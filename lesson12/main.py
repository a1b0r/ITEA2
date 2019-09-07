import telebot
from config import TOKEN, admin_ids


bot = telebot.TeleBot(TOKEN)

def check_for_admin(message):
    if message.text == "admin":
        return True


@bot.message_handler(func=check_for_admin)
def hello(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

list_of_nums = ['1', '2', '3', '4', '5', '6']
@bot.message_handler(commands=['start'])
def keyboard_example(message):
    message_kb = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                                   resize_keyboard=True,
                                                   row_width=3)

    message_kb.add(*list_of_nums)
    bot.send_message(message.chat.id,
                     'keyboard example',
                     reply_markup=message_kb)

    inline_kb = telebot.types.InlineKeyboardMarkup()
    buttons_list = []
    for i in range(21):
        buttons_list.append(
            telebot.types.InlineKeyboardButton(text=f'text_{i}',
                                               callback_data=f'house_{i}')
        )
    inline_kb.add(*buttons_list)
    bot.send_message(chat_id=message.chat.id,
                     text='Inline_kb example',
                     reply_markup=inline_kb)


@bot.callback_query_handler(func=lambda call: call.data and
                            call.data.split('_')[0] == 'house')
def callback_example(call):
    print(call)


if __name__ == "__main__":
    print("Bot started")
    bot.polling(none_stop=True)