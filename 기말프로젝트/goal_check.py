from pico2d import *
import gfw
import ball
import goal
import score
import math

ball_radius = 20

def collides_distance(a1, a2, b):
    a1x,a1y = a1
    a2x, a2y = a2
    bx,by = b
    if a1x >= bx + ball_radius and a1y > by + ball_radius:
        print("1골")
        return 1
    elif a2x <= bx - ball_radius and a2y > by + ball_radius:
        print("2골")
        return 2
    else:
        return 0


def check_collision():
    global goal1pos, goal2pos, ballpos
    goal1pos = goal.image1.w, goal.image1.h + get_canvas_height() // 2 - 225
    goal2pos =get_canvas_width() - goal.image2.w, goal.image1.h + get_canvas_height() // 2 - 225
    ballpos = ball.pos
    check = collides_distance(goal1pos, goal2pos, ballpos)
    return check

