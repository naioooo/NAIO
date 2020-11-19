from pico2d import *
import gfw
import random

MOVE_POS = 300

GRAVITY = 0.2

def init():
    global image, pos, delta_x, delta_y, radius
    image = gfw.image.load('res/ball1.png')
    pos = get_canvas_width() // 2, get_canvas_height() // 2
    delta_x, delta_y = 0, 0
    radius = image.w // 2


def update():
    global pos, delta_x, delta_y
    x, y = pos
    x += delta_x * MOVE_POS * gfw.delta_time
    y += delta_y * MOVE_POS * gfw.delta_time
    delta_y -= GRAVITY
    hw, hh = image.w // 2, image.h // 2

    bottom = y - radius
    if bottom < get_canvas_height() // 2 - 225 and delta_y < 0:
        rand = random.randrange(8,9) / 10
        delta_y *= -rand
        if delta_y <= 1:
            delta_y = 0

    pos = x, y


def draw():
    image.draw(*pos)


