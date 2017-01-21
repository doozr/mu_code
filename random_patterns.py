from microbit import *
import random
from math import sin, cos, radians

def get_randoms():
    off = random.randint(0, 360)
    speed = random.randint(-90, 90)
    drift = random.randint(0 - abs(speed), abs(speed))
    return off, speed, drift

x_off, x_speed, x_drift = get_randoms()
y_off, y_speed, y_drift = get_randoms()

while True:
    if button_a.was_pressed():
        x_off, x_speed, x_drift = get_randoms()
    if button_b.was_pressed():
        y_off, y_speed, y_drift = get_randoms()
    for y in range(0, 5):
        for x in range(0, 5):
            s = sin(radians(x * x_speed + x_off))
            c = cos(radians(y * y_speed + y_off))
            v = s * c * 4.5 + 4.5
            v = int(min(9, max(0, v)))
            display.set_pixel(x, y, v)
    x_off = (x_off + x_drift) % 360
    y_off = (y_off + y_drift) % 360
    sleep(10)