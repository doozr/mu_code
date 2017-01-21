from microbit import *
import random

star = pin0

tree = [
    pin1,
    pin2,
    pin3,
    pin4,
    pin6,
    pin7,
    pin8,
    pin9,
    pin10,
    pin12
]

tree_size = len(tree)

display.off()
star.write_digital(0)

star_state = [False]

def toggle_star():
    star_state[0] = not star_state[0]
    star.write_digital(1 if star_state[0] else 0)    


def tree_range():
    return range(tree_size)


def tree_range_reverse():
    return reversed(range(tree_size))


def set_tree(fn):
    for ix in tree_range():
        pin = tree[ix]
        pin.write_digital(1 if fn(ix) else 0)
    toggle_star()
    pause()
    

def pause():
    sleep(150)
    

def all_off():
    set_tree(lambda ix: False)


def all_on():
    set_tree(lambda ix: True)


def one_on(x):
    set_tree(lambda ix: x == ix)


def on_up_to(x):
    set_tree(lambda ix: ix <= x)


def on_after(x):
    set_tree(lambda ix: ix > x)


def one_at_a_time():
    for x in tree_range():
        one_on(x)


def one_at_a_time_reverse():
    for x in tree_range_reverse():
        one_on(x)


def alternate_flash():
    for _ in range(10):
        set_tree(lambda ix: ix % 2 == 0)
        set_tree(lambda ix: ix % 2 != 0)


def walking_ants():
    for _ in range(10):
        set_tree(lambda ix: ix % 3 == 0)
        set_tree(lambda ix: (ix - 1) % 3 == 0)
        set_tree(lambda ix: (ix - 2) % 3 == 0)


def walking_ants_reverse():
    for _ in range(10):
        set_tree(lambda ix: (ix - 2) % 3 == 0)
        set_tree(lambda ix: (ix - 1) % 3 == 0)
        set_tree(lambda ix: ix % 3 == 0)


def incremental_turn_on_off():
    for x in tree_range():
        on_up_to(x)

    for x in tree_range():
        on_after(x)


def incremental_turn_on_off_reverse():
    for x in tree_range_reverse():
        on_after(x)

    for x in tree_range_reverse():
        on_up_to(x)


def blink():
    for _ in range(10):
        all_on()
        all_off()


def down_wipe():
    layers = [0, 2, 5, 9]
    for l in layers:
        on_up_to(l)
     
    for l in layers:
        on_after(l)


def up_wipe():
    layers = [5, 2, 0, -1]
    for l in layers:
        on_after(l)
     
    for l in layers:
        on_up_to(l)
        

actions = [
    one_at_a_time,
    one_at_a_time_reverse,
    alternate_flash,
    incremental_turn_on_off,
    incremental_turn_on_off_reverse,
    blink,
    walking_ants,
    walking_ants_reverse,
    down_wipe,
    up_wipe
]

while True:
    random.choice(actions)()
