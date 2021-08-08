import random
import pafy
from pytube.__main__ import YouTube
import vlc
import time
from pytube import Playlist

p=Playlist(input("Enter youtube playlist: "))
choice=int(input ("Choose:\n   1. Download entire playlist\n   2. Play shuffle\n"))
no=p.length
if choice==1:
    for video in p.videos:
        video.streams.first().download()
elif choice==2:
    random.seed()
    while True:
        url=(p.video_urls)[random.randrange(1,no)]
        video = pafy.new(url)
        print(video.title)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        time.sleep(YouTube(url).length)