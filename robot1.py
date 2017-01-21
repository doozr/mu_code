from microbit import *

r1 = pin8
r2 = pin12
l1 = pin0
l2 = pin16

def forward():
    r1.write_digital(0)
    r2.write_digital(1)
    l1.write_digital(0)
    l2.write_digital(1)

def backward():
    r1.write_digital(1)
    r2.write_digital(0)
    l1.write_digital(1)
    l2.write_digital(0)

def left():
    r1.write_digital(0)
    r2.write_digital(1)
    l1.write_digital(1)
    l2.write_digital(0)

def right():
    r1.write_digital(1)
    r2.write_digital(0)
    l1.write_digital(0)
    l2.write_digital(1)

def stop():
    r1.write_digital(1)
    r2.write_digital(1)
    l1.write_digital(1)
    l2.write_digital(1)
    
def coast():
    r1.write_digital(0)
    r2.write_digital(0)
    l1.write_digital(0)
    l2.write_digital(0)

def right_detected():
    return pin1.read_analog() > 512
    
def left_detected():
    return pin2.read_analog() > 512

moving = False
while True:
    rd = right_detected()
    ld = left_detected()
    
    if not ld and not rd:
        forward()
        moving = True
        display.show("F")
    elif ld:
        left()
        moving = True
        display.show("L")
    elif rd:
        right()
        moving = True
        display.show("R")
    elif moving:
        stop()
        moving = False
        display.show("S")
    else:
        coast()
        display.show("C")
    sleep(2)