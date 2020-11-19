from pico2d import *
import gfw


class Player:

    def __init__(self):

        self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2 - 200
        self.pos = self.x, self.y
        self.dx = 0
        self.speed = 200
        self.image =  gfw.image.load('res/pikacu1.png')


    def update(self):
        self.x += self.dx * gfw.delta_time * self.speed
        self.pos = self.x, self.y



    def draw(self):
        self.image.draw(*self.pos)

    def handle_event(self, e):

        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 1
            elif e.key == SDLK_RIGHT:
                self.dx += 1
            elif e.key == SDLK_UP:
                pass
            elif e.key == SDLK_DOWN:
                pass

        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 1
            elif e.key == SDLK_RIGHT:
                self.dx -= 1
            elif e.key == SDLK_UP:
                pass
            elif e.key == SDLK_DOWN:
                pass

