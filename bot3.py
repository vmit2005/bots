import telebot
token='6095966259:AAG6CZs49RejaIhQTjfaSzwnWozEgUyyRW4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.polling()