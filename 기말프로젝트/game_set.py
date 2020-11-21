from pico2d import *
import gfw


def handle_event(e):
    global game_start
    if e.type == SDLK_SPACE:
        game_start = True

def init():
    global game_start
    game_start = True

def update():
    global game_start
    game_start = game_start





