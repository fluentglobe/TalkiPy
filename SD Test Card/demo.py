import socket
import network
import gc
import os
import lcd, image
import machine
from board import board_info
from fpioa_manager import fm

fm.register(board_info.WIFI_RX, fm.fpioa.UART2_TX)
fm.register(board_info.WIFI_TX, fm.fpioa.UART2_RX)
uart = machine.UART(machine.UART.UART2, 115200, timeout=1000, read_buf_len=4096)
nic = network.ESP8285(uart)

def connect_wifi(name = "Right Here A", password = "right here right now"):
    nic.connect(name,password)

def download_sample_jpeg(domain = "dl.sipeed.com"):
    sock = socket.socket()
    addr = socket.getaddrinfo(domain, 80)[0][-1]
    sock.connect(addr)
    sock.send('''GET /MAIX/MaixPy/assets/Alice.jpg HTTP/1.1
    Host: dl.sipeed.com
    cache-control: no-cache

    ''')

    img = b""
    sock.settimeout(5)
    while True:
        data = sock.recv(4096)
        if len(data) == 0:
            break
        print("rcv:", len(data))
        img = img + data
    return img

def save_jpg(img, img_path = "/sd/Alice.jpg"):
    print(len(img))
    img = img[img.find(b"\r\n\r\n")+4:]
    print(len(img))
    print("save to", img_path)
    f = open(img_path,"wb")
    f.write(img)
    f.close()
    print("save ok")

def display_jpg(img_path = "/sd/Alice.jpg"):
    print("display")
    img = image.Image(img_path)
    lcd.init()
    lcd.display(img)
