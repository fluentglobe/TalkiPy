import gc
import uos
import os
import sys
import machine
from board import board_info
from fpioa_manager import fm
from pye_mp import pye
from Maix import FPIOA, GPIO

sys.path.append('.')

# chdir to "/sd" or "/flash"
devices = os.listdir("/")
if "sd" in devices:
    os.chdir("/sd")
    sys.path.append('/sd')
else:
    os.chdir("/flash")
sys.path.append('/flash')

# detect boot.py
boot_py = '''
from fpioa_manager import *
import os, Maix, lcd, image
from Maix import FPIOA, GPIO

test_pin=16
fpioa = FPIOA()
fpioa.set_function(test_pin,FPIOA.GPIO7)
test_gpio=GPIO(GPIO.GPIO7,GPIO.IN)
lcd.init(color=(255,0,0))
lcd.draw_string(100,120, "Hello, my name is Talki!", lcd.WHITE, lcd.RED)
if test_gpio.value() == 0:
    print('PIN 7 pulled down, enter test mode')
    import sensor
    import image
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.run(1)
    lcd.freq(16000000)
    while True:
        img=sensor.snapshot()
        lcd.display(img)
'''

flash_ls = os.listdir()
if (not "boot.py" in flash_ls) :
    f = open("boot.py", "wb")
    f.write(boot_py)
    f.close()

# https://www.coolgenerator.com/ascii-text-generator TALKIPY
banner = '''
 _________  ________  ___       ___  __    ___  ________  ___    ___
|\___   ___\\   __  \|\  \     |\  \|\  \ |\  \|\   __  \|\  \  /  /|
\|___ \  \_\ \  \|\  \ \  \    \ \  \/  /|\ \  \ \  \|\  \ \  \/  / /
     \ \  \ \ \   __  \ \  \    \ \   ___  \ \  \ \   ____\ \    / /
      \ \  \ \ \  \ \  \ \  \____\ \  \\ \  \ \  \ \  \___|\/  /  /
       \ \__\ \ \__\ \__\ \_______\ \__\\ \__\ \__\ \__\ __/  / /
        \|__|  \|__|\|__|\|_______|\|__| \|__|\|__|\|__||\___/ /
                                                        \|___|/

Official Site : https://fluentglobe.com/talki
Store         : https://thepia.com/talki
'''
print(banner)

# run boot.py
import boot
