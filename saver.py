from pytube import YouTube
import os


def download(message):
    YouTube(message).streams.first().download()


def findVideo():
    files = os.listdir()
    files.sort(key=os.path.getctime)
    file = files[-1]
    # new_file = file.replace(' ', '_')
    # os.rename(file, new_file)
    return file

