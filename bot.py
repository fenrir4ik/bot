import telebot



bot = telebot.TeleBot("1093407058:AAEmG84mCBHEVX3Mt1raN4xDN94LOcB913Y")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Я юзлесс, но напишите 'Привет'")

@bot.message_handler(content_types=['text'])
def msg(message):
    if (message.text == "Привет"):
        bot.send_photo(message.chat.id, open('1.jpg', 'rb'))

bot.polling()
