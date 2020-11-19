from pico2d import *
import gfw

GRAVITY = 0.5

class Player:

    def __init__(self):

        self.x, self.y = get_canvas_width() // 2 - 200, get_canvas_height() // 2 - 200
        self.pos = self.x, self.y
        self.dx = 0
        self.dy = 0
        self.speed = 200
        self.image =  gfw.image.load('res/pikacu1.png')
        self.jump = False
        self.jump_power = 0
        self.jump_direction = 0
        self.radius = self.image.w // 2
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2

    def jump_check(self):
        if self.jump == True:
            if self.jump_direction == 1:
                if self.jump_power <= 0:
                    self.jump_direction = 2
                self.dy =  self.jump_power
                self.jump_power -= GRAVITY

            elif self.jump_direction == 2:
                if self.y <= get_canvas_height() // 2 - 200:
                    self.jump_direction = 0
                    self.jump_power = 0
                    self.dy = 0
                    self.y =  get_canvas_height() // 2 - 200
                    self.jump = False

                self.dy = self.jump_power
                self.jump_power -= GRAVITY


    def move_check(self):
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2


    def update(self):
        self.move_check()
        self.jump_check()
        self.x += self.dx * gfw.delta_time * self.speed
        self.y += self.dy * gfw.delta_time * (self.speed // 2)
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
                if self.jump == False:
                    self.jump = True
                    self.jump_power = 10
                    self.jump_direction = 1
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

