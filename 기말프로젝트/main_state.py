from pico2d import *
import gfw
import ball
from player import Player
from background import Background

def enter():
    gfw.world.init(['bg', 'ball', 'player'])

    bg = Background('bg.jpg')
    gfw.world.add(gfw.layer.bg, bg)

    ball.init()
    gfw.world.add(gfw.layer.ball, ball)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)


def exit():
    pass


def update():
    gfw.world.update()



def draw():
    gfw.world.draw()


def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()
