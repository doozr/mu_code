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

arrangement = [
    [0],
    [1, 2],
    [5, 4, 3],
    [6, 7, 8, 9]
]


star_state = [False]
star.write_digital(0)

display.off()

def toggle_star():
    star_state[0] = not star_state[0]
    star.write_digital(1 if star_state[0] else 0)


def pause():
    sleep(200)


def combine_indexes(t):
    return (zip(*x) for x in zip(arrangement, t))


def concatenate_branches(t):
    tt = []
    for b in t:
        tt += b
    return tt


def get_light_values(t):
    t = combine_indexes(t)
    t = concatenate_branches(t)
    return [x[1] for x in sorted(t)]


def set_lights(*grid):
    for pin, value in zip(tree, get_light_values(list(grid))):
        pin.write_digital(value)
    toggle_star()
    pause()

