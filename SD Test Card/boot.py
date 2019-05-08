from fpioa_manager import *
import os, Maix, lcd, image, status
from Maix import FPIOA, GPIO

lcd.init(color=(255,0,0))
lcd.draw_string(50,120, "Hello, my name is Talki!", lcd.WHITE, lcd.RED)
status.show_camera()
