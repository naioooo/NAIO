from pico2d import *
import gfw


def handle_event(e):
    global game_start,sound
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_SPACE:
            if game_start == False:
                game_start = True
                sound.repeat_play()


def init():
    global game_start, sound
    sound = load_music('res/bgm.mp3')
    sound.set_volume(20)
    game_start = False

def update():
    if game_start == False:
        sound.stop()





