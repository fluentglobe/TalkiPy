import video, sensor, image, lcd, time
import KPU as kpu

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
sensor.run(1)

lcd.clear()
lcd.draw_string(100,96,"MobileNet Demo")
lcd.draw_string(100,112,"Loading labels...")
f = open('labels.txt','r')
labels = f.readlines()
f.close()

lcd.draw_string(100,112,"Loading kmodel...")
task = kpu.load(0x200000)
lcd.draw_string(100,112,"ready.           ")

# a = kpu.deinit(task)
# lcd.clear()

def run_camera():
    clock = time.clock()
    tim = time.ticks_ms()

    v = video.open("/sd/capture.avi", record=1, interval=200000, quality=50)

    while(time.ticks_diff(time.ticks_ms(), tim) < 60000):
        img = sensor.snapshot()
        clock.tick()
        fmap = kpu.forward(task, img)
        fps=clock.fps()
        plist=fmap[:]
        pmax=max(plist)
        max_index=plist.index(pmax)
        a = lcd.display(img, oft=(0,0))
        lcd.draw_string(0, 224, "%.2f:%s                            "%(pmax, labels[max_index].strip()))
        print(pmax, labels[max_index].strip())

    print("done.")
    v.record_finish()
