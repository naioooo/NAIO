from pico2d import *
import gfw
import random

MOVE_POS = 300

GRAVITY = 0.1

def init():
    global image, pos, dx, dy, radius, x,y, width, height, image_sprite, time, fidx
    image = gfw.image.load('res/ball1.png')
    image_sprite = gfw.image.load('res/ball.png')
    pos = get_canvas_width() // 2, get_canvas_height() // 2
    x, y = pos
    dx, dy = 0, 0
    radius = image.w // 2

    width = get_canvas_width()
    height = get_canvas_height()

    time = 0
    fidx = 0

def reset():
    global pos, dx, dy, x, y, time, fidx
    pos = width // 2,height // 2
    x, y = pos
    dx, dy = 0, 0
    time = 0
    fidx = 0

def update():
    global pos, dx, dy, x, y, width, time, fidx

    x, y = pos
    x += dx * MOVE_POS * gfw.delta_time
    y += dy * MOVE_POS * gfw.delta_time
    dy -= GRAVITY

    hw, hh = image.w // 2, image.h // 2

    left, right = x - radius,  x + radius
    bottom , top = y - radius, y + radius
    if left <= 0:
        dx = -dx
        x = radius
    elif right >= width:
        dx = -dx
        x = width - radius



    # 마찰력 구현
    if bottom < height // 2 - 225:
        if dx >= 0.5:
            dx -= 0.5
        elif dx <= -0.5:
            dx += 0.5

        if dx < 0.5 and dx > 0.0:
            dx -= 0.1
        elif dx > -0.5 and dx < 0.0:
            dx += 0.1
        if dx < 0.1 and dx > -0.1:
            dx = 0.0
    # 골대맞을때 구현
    if bottom <= 150 + height // 2 - 225 and top >= 150 + height // 2 - 225 and left <= 60  and dx < 0:
        dx = -dx
        x = 60
    elif bottom <= 150 + height // 2 - 225 and top >= 150 + height // 2 - 225  and right >= width - 60 and dx > 0:
        dx = -dx
        x = width - 60

    #골대 위로 떨어질때
    if bottom >= 150 + height // 2 - 225 and bottom <= 155 + height // 2 - 225 and left <= 60 and dy < 0:
        rand = random.randrange(8, 9) / 10
        dy *= -rand
    elif bottom >= 150 + height // 2 - 225 and bottom <= 155 + height // 2 - 225 and right >= width - 60 and dy < 0:
        rand = random.randrange(8, 9) / 10
        dy *= -rand

    if bottom < height // 2 - 225 and dy < 0:
        rand = random.randrange(8,9) / 10
        dy *= -rand
        if dy <= 1:
            dy = 0


    if bottom < height // 2 - 225:
        y =  get_canvas_height() // 2 - 225 + radius

    pos = x, y
    if dx <= -0.2 or dx >= 0.2:
        time += gfw.delta_time
        frame = time * 5
        fidx = int(frame) % 5

def draw():
    global  dx, dy, time, fidx, pos

    sx = fidx * 42
    image_sprite.clip_draw(sx, 0, 42, 40, *pos)



