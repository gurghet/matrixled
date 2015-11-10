from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix
import time, sys
import random
import temphum

pilImage = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(pilImage)
m = RGBMatrix(32)


def next_frame():
    draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 0))
    font = ImageFont.truetype('font/alterebro-pixel-font.ttf', 12)
    draw.text((0, 0), "hello this is a test string\n on 2 lines",
              fill=(255, 255, 0), font=font)


def get_temp_hum():
    sys.path.append('/home/pi/pygpiodht22')
    pi = temphum.pi()
    s = temphum.sensor(pi, 6)
    s.trigger()
    time.sleep(0.2)
    ret_val = (s.temperature(), s.humidity())
    s.cancel()
    pi.stop()
    return ret_val


while True:
    nf = m.CreateFrameCanvas()
    next_frame()
    for y in range(0, 31):
        for x in range(0, 31):
            c = pilImage.getpixel((x, y))
            nf.SetPixel(x, y, c[0], c[1], c[2])
    m.SwapOnVSync(nf)
    time.sleep(1)
