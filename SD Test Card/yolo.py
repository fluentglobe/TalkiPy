import sensor
import image
import lcd
import time
import KPU as kpu

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

def run_camera():
    task = kpu.load(0x300000) # you need put model(face.kfpkg) in flash at address 0x300000
    # task = kpu.load("/sd/face.kmodel")
    anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
    a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
    while(True):
        img = sensor.snapshot()
        code = kpu.run_yolo2(task, img)
        if code:
            for i in code:
                print(i)
                a = img.draw_rectangle(i.rect())
        a = lcd.display(img)
    a = kpu.deinit(task)



# Binocular
# https://bbs.sipeed.com/t/topic/565

def run_binocular():    
    sensor.binocular_reset()
    sensor.shutdown(False)
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.shutdown(True)
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
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
