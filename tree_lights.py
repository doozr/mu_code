from microbit import *

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


def set_star(on):
    star.write_digital(1 if on else 0)


def tree_range():
    return range(tree_size)


def tree_range_reverse():
    return range(tree_size, 0, -1)


def set_tree(fn):
    for ix in tree_range():
        pin = tree[ix]
        pin.write_digital(1 if fn(ix) else 0)


def all_off():
    set_tree(lambda ix: False)
    set_star(False)


def all_on():
    set_tree(lambda ix: True)
    set_star(True)


def one_on(x):
    set_tree(lambda ix: x == ix)


def on_up_to(x):
    set_tree(lambda ix: ix <= x)


def on_after(x):
    set_tree(lambda ix: ix > x)


def one_at_a_time():
    for x in tree_range():
        one_on(x)
        set_star(x % 2 == 0)
        sleep(50)

    for x in tree_range_reverse():
        one_on(x)
        set_star(x % 2 == 0)
        sleep(50)


def alternate_flash():
    set_tree(lambda ix: ix % 2 == 0)
    set_star(True)
    sleep(100)

    set_tree(lambda ix: ix % 2 != 0)
    set_star(False)
    sleep(100)


def walking_ants():
    set_tree(lambda ix: ix % 3 == 0)
    sleep(100)
    set_tree(lambda ix: (ix - 1) % 3 == 0)
    sleep(100)
    set_tree(lambda ix: (ix - 2) % 3 == 0)
    sleep(100)


def incremental_turn_on_off(reverse):
    r = tree_range_reverse() if reverse else tree_range()
    for x in r:
        on_up_to(x)
        set_star(x % 2 == 0)
        sleep(50)

    r = tree_range_reverse() if reverse else tree_range()
    for x in r:
        on_after(x)
        set_star(x % 2 == 0)
        sleep(50)


def blink():
    all_on()
    set_star(True)
    sleep(100)
    all_off()
    set_star(False)
    sleep(100)


while True:
    for _ in range(2):
        one_at_a_time()

    for _ in range(8):
        alternate_flash()

    for _ in range(2):
        incremental_turn_on_off(False)

    for _ in range(6):
        blink()

    for _ in range(2):
        incremental_turn_on_off(True)

    for _ in range(8):
        alternate_flash()

    for x in range(6):
        walking_ants()
        set_star(x % 2 == 0)
