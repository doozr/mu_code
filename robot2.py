from microbit import *

r1 = pin8
r2 = pin12
l1 = pin0
l2 = pin16

def forward():
    r1.write_digital(1)
    r2.write_digital(0)
    l1.write_digital(1)
    l2.write_digital(0)

def backward():
    r1.write_digital(0)
    r2.write_digital(1)
    l1.write_digital(0)
    l2.write_digital(1)

def right():
    r1.write_digital(1)
    r2.write_digital(0)
    l1.write_digital(0)
    l2.write_digital(0)

def left():
    r1.write_digital(0)
    r2.write_digital(0)
    l1.write_digital(1)
    l2.write_digital(0)

def brake():
    r1.write_digital(1)
    r2.write_digital(1)
    l1.write_digital(1)
    l2.write_digital(1)
    
def stop():
    r1.write_digital(0)
    r2.write_digital(0)
    l1.write_digital(0)
    l2.write_digital(0)

def left_detected():
    return pin1.read_analog() < 512
    
def right_detected():
    return pin2.read_analog() < 512

def neither_detected():
    return not left_detected() and not right_detected()

def both_detected():
    return left_detected() and right_detected()

while True:
    if neither_detected():
        forward()
        display.show("F")
        
    elif right_detected():
        left()
        display.show("L")
        
    elif left_detected():
        right()
        display.show("R")

    sleep(2)