from pico2d import *
import gfw

class Score:
    def __init__(self, right, y):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.right, self.y = right, y
        self.image = gfw.image.load('res/number_24x32.png')
        self.digit_width = self.image.w // 10
        self.setscore1 = 0
        self.setscore2 = 0
        self.reset()

    def reset(self):
        self.score1 = 0
        self.score2 = 0
        self.display1 = 0
        self.display2 = 0

    def draw(self):
        x = self.right
        score1, score2  = self.display1, self.display2
        if self.display1 == 0:
            self.image.clip_draw(0, 0, self.digit_width, self.image.h, x + 100, self.y)
        if self.display2 == 0:
            self.image.clip_draw(0, 0, self.digit_width, self.image.h, x - 150, self.y)

        while score1 > 0:
            digit = score1 % 10
            sx = digit * self.digit_width
            # print(type(sx), type(digit), type(self.digit_width))
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x + 100, self.y)
            score1 //= 10
        x = self.right
        while score2 > 0:
            digit = score2 % 10
            sx = digit * self.digit_width
            # print(type(sx), type(digit), type(self.digit_width))
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x - 150, self.y)
            score2 //= 10

    def update(self):
        self.setscore1 = self.display1
        self.setscore2 = self.display2
        if self.display2 < self.score2:
            self.display2 += 1
        if self.display1 < self.score1:
            self.display1 += 1


