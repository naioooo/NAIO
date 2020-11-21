from pico2d import *
import gfw

GRAVITY = 0.5

class Player2:

    def __init__(self):

        self.x, self.y = get_canvas_width() // 2 + 200, get_canvas_height() // 2 - 200
        self.pos = self.x, self.y
        self.dx = 0
        self.dy = 0
        self.speed = 200
        self.image =  gfw.image.load('res/pikachu2_sprite.png')
        self.jump = False
        self.jump_power = 0
        self.jump_direction = 0
        self.radius = 32
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2

        self.time = 0
        self.fidx = 0

    def reset(self):
        self.x, self.y = get_canvas_width() // 2 + 200, get_canvas_height() // 2 - 200
        self.pos = self.x, self.y
        self.dy = 0
        self.jump = False
        self.jump_power = 0
        self.jump_direction = 0
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2
        self.time = 0
        self.fidx = 0

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

        self.time += gfw.delta_time
        frame = self.time * 7
        self.fidx = int(frame) % 7




    def draw(self):
        sx = self.fidx * 65
        self.image.clip_draw(sx, 0, 65, 58, *self.pos)

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

