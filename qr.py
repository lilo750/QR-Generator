from random import randrange
from PIL import Image
import qrcode
import os
import time

link = input("write your link: ")
random = randrange(100)

if "http" in link.lower():
    img = qrcode.make(link)
    type(img)  # qrcode.image.pil.PilImage
    img.save(f"QR_{random}.png")
    os.system(f"QR_{random}.png")
else:
    print("enter your link with https or https\n Ex:https:yourlink.com")
    time.sleep(5)
