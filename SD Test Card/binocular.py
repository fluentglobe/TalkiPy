# https://bbs.sipeed.com/t/topic/565

import sensor
import image
import lcd
import time

lcd.init()
sensor.binocular_reset()
sensor.shutdown(False)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.shutdown(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

def run_camera():
    sensor.run(1)
    while True:
        sensor.shutdown(False)
        img=sensor.snapshot()
        lcd.display(img)
        time.sleep_ms(100)
        sensor.shutdown(True)
        img=sensor.snapshot()
        lcd.display(img)
        time.sleep_ms(100)
