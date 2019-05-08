from fpioa_manager import *
import os, Maix, lcd, image, sensor
from Maix import FPIOA, GPIO

def show_hello():
    lcd.init(color=(255,0,0))
    lcd.draw_string(50,120, "Hello, my name is Talki!", lcd.WHITE, lcd.RED)

def show_camera():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_auto_exposure(True, 10)
    sensor.run(True)
    lcd.freq(16000000)
    img = sensor.snapshot()
    sensor.run(0)
    lcd.display(img)

def show_status():
    test_pin=16
    fpioa = FPIOA()
    fpioa.set_function(test_pin, FPIOA.GPIO7)
    test_gpio = GPIO(GPIO.GPIO7,GPIO.IN)
    if test_gpio:
        print("test pin 16 shorted?")
