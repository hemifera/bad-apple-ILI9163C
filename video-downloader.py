import os
from pytube import YouTube
video_url = "https://youtu.be/FtutLA63Cp8"

yt = YouTube(video_url)
files = yt.streams.filter(file_extension='mp4')
stream = yt.streams.get_by_itag(18)
print("Trying to download the video as bad_apple.mp4")
try:
    stream.download(filename="bad_apple.mp4")
    print(f"{yt.title} downloaded successfully!") 
except Exception as ex:
    print("OH NO! Something happened!")
    print(f"ERROR: {ex}")
    
