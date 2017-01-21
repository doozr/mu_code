from microbit import *

red_light = pin8
amber_light = pin12
green_light = pin16

dial = pin1

buzzer = pin0

request = button_b
button_pressed = False

dont_walk = Image("00900:"
                  "99999:"
                  "00900:"
                  "09090:"
                  "09090")

walk = Image("00900:"
             "09990:"
             "90909:"
             "99090:"
             "00090")

lights_stop = (1, 0, 0)
lights_ready = (1, 1, 0)
lights_go = (0, 0, 1)
lights_slow = (0, 1, 0)


def read_speed():
    return dial.read_analog()


def set_lights(red, amber, green):
    red_light.write_digital(red)
    amber_light.write_digital(amber)
    green_light.write_digital(green)


def set_walk(image):
    display.show(image)


def show_button_pressed(is_pressed):
    if is_pressed:
        display.set_pixel(4, 0, 9)
    else:
        display.set_pixel(4, 0, 0)


def set_beep(on):
    if on:
        buzzer.write_analog(1023)
    else:
        buzzer.write_analog(0)


class State(object):
    def __init__(self, lights=lights_stop, walk=dont_walk, delay=1,
                 beep=False, cancel_button=False, next_state=False):
        self.lights = lights
        self.walk = walk
        self.delay = delay
        self.beep = beep
        self.cancel_button = cancel_button
        self.next_state = next_state

    def get_next_state(self):
        return self.next_state()

    def set_outputs(self):
        set_lights(*self.lights)
        set_walk(self.walk)
        set_beep(self.beep)


STATE_STOP_NOWALK = State(
    lights=lights_stop,
    walk=dont_walk,
    delay=3,
    next_state=lambda: STATE_READY)
    
STATE_STOP_HURRY = State(
    lights=lights_stop,
    walk=walk,
    delay=4,
    beep=False,
    cancel_button=True,
    next_state=lambda: STATE_STOP_NOWALK)
    
STATE_STOP_WALK = State(
    lights=lights_stop,
    walk=walk,
    delay=6,
    beep=True,
    cancel_button=True,
    next_state=lambda: STATE_STOP_HURRY)
    
STATE_STOP_WAIT = State(
    lights=lights_stop,
    walk=dont_walk,
    delay=3,
    next_state=lambda: STATE_STOP_WALK)
    
STATE_SLOW = State(
    lights=lights_slow,
    walk=dont_walk,
    delay=1,
    next_state=lambda: STATE_STOP_WAIT if button_pressed else STATE_STOP)
    
STATE_GO = State(
    lights=lights_go,
    walk=dont_walk,
    delay=10,
    next_state=lambda: STATE_SLOW)
    
STATE_READY = State(
    lights=lights_ready,
    walk=dont_walk,
    delay=1,
    next_state=lambda: STATE_GO)
    
STATE_STOP = State(
    lights=lights_stop,
    walk=dont_walk,
    delay=10,
    next_state=lambda: STATE_READY)

state = STATE_STOP
delay = state.enter_state()

while True:
    speed = read_speed()
    button_pressed = button_pressed or request.was_pressed()
    if delay == 0:
        state = state.get_next_state()
        state.set_outputs()
        delay = state.delay
        if state.cancel_button:
            button_pressed = False
    else:
        delay = delay - 1
    show_button_pressed(button_pressed)
    sleep(speed)
