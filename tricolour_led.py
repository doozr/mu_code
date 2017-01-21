from microbit import *

MAX=250
STEP=5

def pin_pressed(p):
    def _pressed():
        return p.read_digital() == 1
    return _pressed

red_pressed = pin_pressed(pin8)
green_pressed = pin_pressed(pin12)
blue_pressed = pin_pressed(pin16)
max_pressed = button_a.was_pressed
clear_pressed = button_b.was_pressed

def update_pin(p):
    def _update(v):
        v = min(MAX, max(0, v))
        p.write_analog(v)
    return _update

update_red = update_pin(pin0)
update_green = update_pin(pin1)
update_blue = update_pin(pin2)

def update_display(r, g, b):
    bucket = MAX // 5
    def update_column(x, v):
        for y in range(4, -1, -1):
            if v == 0:
                display.set_pixel(x, y, 0)
            elif v < bucket:
                display.set_pixel(x, y, v * 9 // bucket)
                v = 0
            else:
                display.set_pixel(x, y, 9)
                v = v - bucket
    update_column(0, r)
    update_column(2, g)
    update_column(4, b)

def update(r, g, b):
    update_red(r)
    update_blue(b)
    update_green(g)
    update_display(r, g, b)

def increment(v):
    return (v + STEP) % MAX

red = 0
green = 0
blue = 0

while True:            
    sleep(100)

    do_update = False
    if red_pressed():
        red = increment(red)
        do_update = True
        
    if green_pressed():
        green = increment(green)
        do_update = True
    
    if blue_pressed():
        blue = increment(blue)
        do_update = True
        
    if max_pressed():
        red = MAX
        green = MAX
        blue = MAX
        do_update = True
        
    if clear_pressed():
        red = 0
        green = 0
        blue = 0
        do_update = True
    
    if do_update:
        update(red, green, blue)