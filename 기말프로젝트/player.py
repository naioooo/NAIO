from pico2d import *
import gfw

GRAVITY = 0.5

class Player:

    def __init__(self):

        self.x, self.y = get_canvas_width() // 2 - 200, get_canvas_height() // 2 - 197
        self.pos = self.x, self.y
        self.dx = 0
        self.dy = 0
        self.speed = 200
        self.image_walk =  gfw.image.load('res/pikachu1_sprite.png')
        self.image = gfw.image.load('res/pikachu1.png')
        self.image_jump = gfw.image.load('res/pikachu_jump1.png')
        self.jump = False
        self.jump_power = 0
        self.jump_direction = 0
        self.radius = 32
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2
        self.jump_sound = load_wav('res/pikachu_jump.wav')
        self.jump_sound.set_volume(10)
        self.time = 0
        self.fidx = 0
        self.keycount = 0

    def reset(self):
        self.x, self.y = get_canvas_width() // 2 - 200, get_canvas_height() // 2 - 200
        self.pos = self.x, self.y
        self.dy = 0
        self.dx = 0
        self.jump = False
        self.jump_power = 0
        self.jump_direction = 0
        self.move_distance = (self.dx) ** 2 + (self.dy) ** 2
        self.time = 0
        self.fidx = 0
        self.keycount = 0

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
        if self.x < self.radius:
            self.x = self.radius
        self.y += self.dy * gfw.delta_time * (self.speed // 2)
        if self.x > get_canvas_width() - self.radius:
            self.x =  get_canvas_width() - self.radius
        self.pos = self.x, self.y

        if self.dx == 1:
            self.time += gfw.delta_time
        elif self.dx == -1:
            self.time -= gfw.delta_time
        frame = self.time * 7
        self.fidx = int(frame) % 7




    def draw(self):


        sx = self.fidx * 65
        if self.jump == False and self.dx == 0:
            self.image.draw(*self.pos)
        elif self.jump == False and self.dx != 0  :
            self.image_walk.clip_draw(sx, 0, 65, 58, *self.pos)
        elif self.jump == True:
            self.image_jump.clip_draw(sx, 0, 65, 58, *self.pos)

    def handle_event(self, e):

        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                if self.dx >= 0:
                    self.dx -= 1
                    self.keycount += 1
            elif e.key == SDLK_d:
                if self.dx <= 0:
                    self.dx += 1
                    self.keycount += 1
            elif e.key == SDLK_w:
                if self.jump == False:
                    self.jump = True
                    self.jump_sound.play()
                    self.jump_power = 10
                    self.jump_direction = 1
                    self.time = 0
                    self.fidx = 0
            elif e.key == SDLK_s:
                pass

        elif e.type == SDL_KEYUP:
            if self.keycount > 0:
                if e.key == SDLK_a:
                    if self.dx <= 0:
                        self.dx += 1
                        self.keycount -= 1
                elif e.key == SDLK_d:
                    if self.dx >= 0:
                        self.dx -= 1
                        self.keycount -= 1
                elif e.key == SDLK_w:
                    pass
                elif e.key ==  SDLK_s:
                    pass

