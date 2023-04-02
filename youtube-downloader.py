from pytube import YouTube
from moviepy.editor import *
from pytube.helpers import install_proxy

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

print("""

 __     _________       _                     _                 _           
 \ \   / /__   __|     | |                   | |               | |          
  \ \_/ /   | |      __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   /    | |     / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |     | |    | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|     |_|     \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_| 
                                made by zenci                                                                                                    """)

def menu():
    print("[1] download a mp4")
    print("[2] change it to a mp3")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        link = input("yt url: ")
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        exit()
    elif option == 2:
        name = input("name of the file: ")
        video = VideoFileClip(name +".mp4")
        video.audio.write_audiofile(name + ".mp3")
        exit()
