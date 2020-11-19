from pico2d import *
import gfw

MOVE_POS = 300


def init():
    global image, pos, delta_x, delta_y, radius
    image = gfw.image.load('res/ball1.png')
    pos = get_canvas_width() // 2, get_canvas_height() // 2 - 140
    delta_x, delta_y = 0, 0
    radius = image.w // 2


def update():
    global pos, delta_x, delta_y
    x, y = pos
    x += delta_x * MOVE_POS * gfw.delta_time
    y += delta_y * MOVE_POS * gfw.delta_time
    hw, hh = image.w // 2, image.h // 2
    x = clamp(hw, x, get_canvas_width() - hw)
    y = clamp(hh, y, get_canvas_height() - hh)
    pos = x, y


def draw():
    image.draw(*pos)


