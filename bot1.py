
import telebot
import urllib.request
import time
import os
"""
Простой бот.
Обнаруживает загрузку в чат фотки и копирует ее на диск.
Никак себя не выдает.

"""

token = '6095966259:AAG6CZs49RejaIhQTjfaSzwnWozEgUyyRW4'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):

    fileid = message.json['photo'][2]['file_id']
    try:
        name_photo = message.json['caption'] + ".jpg"
    except:
        name_photo = f'image{int(time.time())}.jpg'

    s = time.localtime(time.time())
    if not (os.path.exists(f"./{s.tm_year}/{s.tm_mon}/{s.tm_mday}")):
        os.makedirs(f"./{s.tm_year}/{s.tm_mon}/{s.tm_mday}")

    fpth = "https://api.telegram.org/file/bot" + token + "/" + (bot.get_file(fileid)).file_path

    urllib.request.urlretrieve(fpth, f"./{s.tm_year}/{s.tm_mon}/{s.tm_mday}/{name_photo}")
    print(fpth)


bot.polling(none_stop=True)
