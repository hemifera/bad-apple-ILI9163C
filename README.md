# Bad apple!! in the ILI9163C screen (128x128px)
>Bad apple!! from Masayoshi Minoshima

### Origin and reason:
Bad apple!! is the sixth track in the soundtrack of the 1998 bullet hell video game Lotus Land Story from the videgame franchise known as Touhou Project from the software developer Team Shanghai Alice. Bad apple was later animated and to the day, a lot of people had played the song in different screen formats, such as lcd screens, linux terminals, microsoft paint, desmos calculator and even more!

This projects just does the same but in the SPI screen ILI9163C!

It uses [Blavery's LIBtft144 library](https://github.com/BLavery/LIBtft144) to control the screen and adds a few scripts so you just have to follow some directions to even play it yourself!

Playing Bad Apple on the TFT-1.44" screen ILI9163C in a Raspberry Pi 3B+ in the following: video

https://youtu.be/XVJNYHPoZJc

What I'm using:
- Python 3.10.8 
- pip 22.3.1
- RPi.GPIO
- imageio & imageio-ffmpeg
- Pillow
- and its dependencies!

Directions to play Bad apple!

1. Create a python environment and install the dependencies.
```
python3 -m venv env
pip install -r requirements.txt
```

In the following directions you run code that can be used for other instances, so you can reuse the files whichever you like. 

2. Download the video in mp4 format.
```
python3 video-downloader.py
```
3. Iterate each video frame to an image in the bitmap format (.bmp) and save it.
This creates a folder called "frames" and saves everything there!
```
python3 video-to-frame.py
```
4. Reduce each frame to a size that fits the screen (from 480*360px to 120x90px)
```
python3 image-resizer.py
```

5. Let's play it!
```
python3 bad-apple.py
```

This loops the song with a bad practice known as
**while(True)** just so you are aware.
