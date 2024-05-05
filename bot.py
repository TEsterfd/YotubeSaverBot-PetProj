import telebot
from cfg import TOKEN_API
import os
from saver import *

bot = telebot.TeleBot(TOKEN_API)


@bot.message_handler()
def video_send(message):
    try:
        download(message.text)
        fpath = findVideo()
        video = open(fpath, 'rb')
        bot.send_video(message.chat.id, video)
        video.close()
        os.remove(fpath)
    except:
        bot.send_message(message.chat.id, 'Не удалось скачать видео')





    




bot.polling(none_stop=True)