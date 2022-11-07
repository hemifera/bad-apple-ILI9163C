from smartGPIO import GPIO
from lib_tft144 import TFT144
from time import sleep as sleep
import os, sys, spidev
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
RST, CE, DC, LED = 18, 0, 22, 23
# RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
# CE RPI GPIO: 0 or 1 for CE0 / CE1 number (NOT the pin#)
# DC Labeled on board as "A0"   Command/Data select
# LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V

spi = spidev.SpiDev()
TFT = TFT144(GPIO, spi, CE, DC, RST, LED, TFT144.ORIENTATION90, isRedBoard=False)

FRAMES_PER_SECOND = 60
FRAME_LAPSE = 1 / FRAMES_PER_SECOND

frames_folder = os.path.join(os.getcwd(), "reduced_frames")
files_list = os.listdir(frames_folder)
files_list.sort()
conteo = 0
while(True):
    try: 
        for file_index, file_name in enumerate(files_list):
            current_file = os.path.join(frames_folder, file_name)
            TFT.draw_bmp(current_file, 0, 19)
            text = f"{conteo}:{file_name}"
            TFT.put_string(text,0,5,TFT.WHITE,TFT.BLACK, 3)  # std font 3 (default)
        conteo=conteo+1
    except Exception as ex:
        TFT.clear_display(TFT.BLACK)
        
