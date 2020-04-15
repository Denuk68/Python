# Модуль call може виконати будь-яку команду
from subprocess import call
import os
if __name__ == "__main__": 
    downloader


class downloader():
    def menu(self):
        choice = int(input("1. Download single Movie\n2. Yuotube playlist\n0. Exit\n====>>>"))
        return choice

    def download_youtube_single_media(self):
        movie_url = input('Enter movie URL=>')
        movie_info =  "youtube-dl " + movie_url + ' -F'
        call(movie_info, shell=False)
        format = input('Enter Format code : ')
        os.chdir('Downloads')
        download_command = "youtube-dl -f " + format + " " + movie_url + ' -c'
        call(download_command, shell=False) 
        

