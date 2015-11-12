# -*- coding: utf-8 -*-
import ext_temp
import time, sys
sys.path.append('..')
from PIGPIO import pigpio
from pygpiodht22 import DHT22
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix

pilImage = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(pilImage)
m = RGBMatrix(32)


def next_frame():
    draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 0))

    (temp, hum) = get_temp_hum()
    (e_temp, e_hum) = ext_temp.get_temp_hum()

    font = ImageFont.truetype('../font/alterebro-pixel-font.ttf', 16)
    minifont = ImageFont.truetype('../font/Rygarde.ttf', 8)

    draw.text((9, 0), "%(temp)d" % {"temp": e_temp},
              fill=(255, 153, 0), font=minifont)
    draw.text((3, 4), "%(temp).1f\xb0C" % {"temp": temp},
              fill=(255, 255, 0), font=font)
    draw.text((4, 12), "%(hum).1f%%" % {"hum": hum},
              fill=(255, 255, 0), font=font)
    draw.text((9, 26), "%(hum)d" % {"hum": e_hum},
              fill=(255, 153, 0), font=minifont)


def get_temp_hum():
    pi = pigpio.pi()
    s = DHT22.sensor(pi, 6)
    s.trigger()
    time.sleep(0.2)
    ret_val = (s.temperature(), s.humidity())
    s.cancel()
    pi.stop()
    return ret_val


if __name__ == '__main__':
    while True:
        nf = m.CreateFrameCanvas()
        next_frame()
        for y in range(0, 31):
            for x in range(0, 31):
                c = pilImage.getpixel((x, y))
                nf.SetPixel(x, y, c[0], c[1], c[2])
        m.SwapOnVSync(nf)
        time.sleep(1)
