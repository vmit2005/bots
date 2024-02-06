import telebot
from telebot import types
from random import choice
import urllib.request
import time

token = '6095966259:AAG6CZs49RejaIhQTjfaSzwnWozEgUyyRW4'
ranchoise = ["Что за фигню ты несеш?", "Что с этим пареньком?", "Да и пес с ними!", "Не люблю сигнализации!"]
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.username}</b>'
    print(message.from_user.username)
    bot.send_message(message.chat.id,mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello" or message.text.casefold() == "привет":
        bot.send_message(message.chat.id, f"И тебе привет, {message.from_user.username} !", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')

    elif message.text.casefold() == "одеть":
        bot.send_message(message.chat.id, f"Следи за языком. Не одеть, а надеть", parse_mode='html')

    elif message.text.casefold() == "надеть":
        bot.send_message(message.chat.id, f"Следи за языком. Не надеть, а одеть", parse_mode='html')

    elif message.text == "photo":
        photo = open('rebro3.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()

    else:

        # bot.send_message(message.chat.id,message, parse_mode='html')
        bot.send_message(message.chat.id, choice(ranchoise), parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Крутое фото", parse_mode='html')
    print(message)
    fileid = message.json['photo'][2]['file_id']
    try:
        name_photo = message.json['caption']+".jpg"
    except:
        name_photo = f'image{int(time.time())}.jpg'

    print(name_photo)
    print(fileid)
    fpth = "https://api.telegram.org/file/bot" + token + "/" + (bot.get_file(fileid)).file_path
    urllib.request.urlretrieve(fpth, name_photo)
    print(fpth)

    # bot.send_message(message.chat.id, message, parse_mode='html')


bot.polling(none_stop=True)
