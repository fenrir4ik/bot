import telebot



bot = telebot.TeleBot("1093407058:AAEmG84mCBHEVX3Mt1raN4xDN94LOcB913Y")


@bot.message_handler(commands=['cmd'])
def send_welcome(message):
    bot.reply_to(message, "Бот жив ёпта!")


bot.polling()