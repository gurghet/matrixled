from PIL import Image, ImageDraw
from rgbmatrix import RGBMatrix
import time
import random

pilImage = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(pilImage)
m = RGBMatrix(32)

def rr():
    return random.randint(0,31)

def next():
    draw.rectangle((0,0,31,31), fill=(0,0,0), outline=(0,0,0))
    draw.line((rr(),rr(),rr(),rr()), fill=(0,255,0))

while True:
    nf = m.CreateFrameCanvas()
    next()
    for y in range(0, 31):
        for x in range(0, 31):
            c = pilImage.getpixel((x,y))
            nf.SetPixel(x,y,c[0],c[1],c[2])
    m.SwapOnVSync(nf)
    time.sleep(1)
