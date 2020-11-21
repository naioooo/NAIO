from pico2d import *
import gfw



def init():
    global image1, image2, pos1, pos2, width,height

    width = get_canvas_width()
    height = get_canvas_height()
    image1 = gfw.image.load('res/goal.png')
    image2 = gfw.image.load('res/goal2.png')
    pos1 = image1.w//2, image1.h//2 + height // 2 - 225
    pos2 = width - image2.w // 2, image2.h // 2 + height // 2 - 225



def update():
    pass


def draw():
    image1.draw(*pos1)
    image2.draw(*pos2)


