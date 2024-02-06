import telebot
import urllib.request
import os
from bot2Fnctn import *

"""
Бот создающщий коллаж из загруженных фоток.

"""

token = '6095966259:AAG6CZs49RejaIhQTjfaSzwnWozEgUyyRW4'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    username = message.json['from']['username']
    l = (len(message.json['photo'])) - 1
    fileid = message.json['photo'][l]['file_id']
    print(fileid)
    try:
        mjc = message.json['caption']
    except:
        mjc = " "
    if mjc == "img1" or mjc == "img2" or mjc == "img3" or mjc == "img4" or mjc == "img5":
        if not (os.path.exists(f"./{username}")):
            os.makedirs(f"./{username}")
        fpth = "https://api.telegram.org/file/bot" + token + "/" + (bot.get_file(fileid)).file_path
        urllib.request.urlretrieve(fpth, f"./{username}/{mjc}.jpg")
        print(fpth)
        bot.send_message(message.chat.id, f"Фотография загружена в файл {mjc}.jpg", parse_mode='html')

@bot.message_handler(commands=['/privet'])
def userhelp(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")

@bot.message_handler()
def get_user_text(message):

    if message.text == "hello" or message.text.casefold() == "привет":
        bot.send_message(message.chat.id, f"И тебе привет, {message.from_user.username} !", parse_mode='html')
    elif message.text.casefold() == "type1":
        try:
            b,h = img_size(f'{message.from_user.username}/img1.jpg',f'{message.from_user.username}/img2.jpg', f'{message.from_user.username}/img3.jpg', f'{message.from_user.username}/img4.jpg')
            i1=img_size2(f'{message.from_user.username}/img1.jpg',b,h)
            i2 = img_size2(f'{message.from_user.username}/img2.jpg', b, h)
            i3 = img_size2(f'{message.from_user.username}/img3.jpg', b, h)
            i4 = img_size2(f'{message.from_user.username}/img4.jpg', b, h)
            i=merge4(i1,i2,i3,i4)
            bot.send_photo(message.chat.id, i)
            i1.close()
            i2.close()
            i3.close()
            i4.close()
        except:
            bot.send_message(message.chat.id, "А вы загрузили файлы img1.jpg, img2.jpg... img5.jpg ?", parse_mode='html')

    elif message.text.casefold() == "type2":
        try:
            b, h = img_size(f'{message.from_user.username}/img1.jpg', f'{message.from_user.username}/img2.jpg',
                           f'{message.from_user.username}/img3.jpg', f'{message.from_user.username}/img4.jpg')
            b1,h1 =img_size(f'{message.from_user.username}/img5.jpg')
            i1 = img_size2(f'{message.from_user.username}/img1.jpg', b, h)
            i2 = img_size2(f'{message.from_user.username}/img2.jpg', b, h)
            i3 = img_size2(f'{message.from_user.username}/img3.jpg', b, h)
            i4 = img_size2(f'{message.from_user.username}/img4.jpg', b, h)
            i5 = img_size2(f'{message.from_user.username}/img5.jpg', b1, h1)
            i = merge5(i1, i2, i3, i4,i5)
            i1.close()
            i2.close()
            i3.close()
            i4.close()
            i5.close()
            bot.send_photo(message.chat.id, i)
        except:
            bot.send_message(message.chat.id, "А вы загрузили файлы img1.jpg, img2.jpg... img5.jpg ?", parse_mode='html')


    elif message.text.casefold() == "type3":
        try:
            b, h = img_size(f'{message.from_user.username}/img1.jpg', f'{message.from_user.username}/img2.jpg',
                            f'{message.from_user.username}/img3.jpg', f'{message.from_user.username}/img4.jpg')
            b1, h1 = img_size(f'{message.from_user.username}/img5.jpg')
            i1 = img_size2(f'{message.from_user.username}/img1.jpg', b, h)
            i2 = img_size2(f'{message.from_user.username}/img2.jpg', b, h)
            i3 = img_size2(f'{message.from_user.username}/img3.jpg', b, h)
            i4 = img_size2(f'{message.from_user.username}/img4.jpg', b, h)
            i5 = img_size2(f'{message.from_user.username}/img5.jpg', b1, h1)
            i = merge5ellips(i1, i2, i3, i4, i5)
            i1.close()
            i2.close()
            i3.close()
            i4.close()
            i5.close()
            bot.send_photo(message.chat.id, i)
        except:
            bot.send_message(message.chat.id, "А вы загрузили файлы img1.jpg, img2.jpg... img5.jpg ?", parse_mode='html')




    elif message.text.casefold() == "type4":
        try:
            i= merge4diag (f'{message.from_user.username}/img1.jpg', f'{message.from_user.username}/img2.jpg',
                            f'{message.from_user.username}/img3.jpg', f'{message.from_user.username}/img4.jpg')
            bot.send_photo(message.chat.id, i)
        except:
            bot.send_message(message.chat.id, "А вы загрузили файлы img1.jpg, img2.jpg... img5.jpg ?", parse_mode='html')

    elif message.text.casefold()== "/help" or message.text == "/start":
         messs="""
         Бот предназначен для создания коллажей. Сейчас реализованно четыре схемы раскладки фотографий . 
         Для работы с ботом нужно загрузить свои фотографии 5 штук. Просто берете и грузите их в чат . 
         Важно: в окошечко "подпись" под фотографией нужно написать имя файла img1,img2,img3,img4,img5.
         Только такие названия и не повторяясь. Пять файлов пять названий.
         Если все получилось, бот вас проинформирует, например:"Фотография загружена в файл img4.jpg"
         Если есть какое-то сомнение отправьте боту img1 (или img2... img5). Выведет картинку загруженную под этим именем
         Отправьте боту сообщение type1  или type2, type3, type4. Маленькими буквами без кавычек.
         """
         bot.send_message(message.chat.id, messs, parse_mode='html')
    elif message.text.casefold() == "img1":
        try:
            photo = open(f'{message.from_user.username}/img1.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:

            bot.send_message(message.chat.id, "Такого файла нет", parse_mode='html')
    elif message.text.casefold() == "img2":
        try:
            photo = open(f'{message.from_user.username}/img2.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            bot.send_message(message.chat.id, "Такого файла нет", parse_mode='html')
    elif message.text.casefold() == "img3":
        try:
            photo = open(f'{message.from_user.username}/img3.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            bot.send_message(message.chat.id, "Такого файла нет", parse_mode='html')
    elif message.text.casefold() == "img4":
        try:
            photo = open(f'{message.from_user.username}/img4.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            bot.send_message(message.chat.id, "Такого файла нет", parse_mode='html')
    elif message.text.casefold() == "img5":
        try:
            photo = open(f'{message.from_user.username}/img5.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            bot.send_message(message.chat.id, "Такого файла нет", parse_mode='html')


bot.polling(none_stop=True)
