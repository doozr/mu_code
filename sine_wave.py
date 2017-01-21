from microbit import *
from math import sin, radians

offset = 0

while True:
    display.clear()
    for x in range(0, 5):
        y = sin(radians(x * 90 + offset)) * 2.5 + 2.5
        y = min(4, max(0, y))
        display.set_pixel(x, int(y), 9)
    offset = (offset + 10) % 360
    sleep(10)
