from pico2d import *
import gfw
import ball
from player import Player
from player2 import Player2


import math

elasticity = 0.5

def data_stream(a, b):
    adx, ady = a.dx, a.dy
    bdx, bdy = b.dx, b.dy

    angle = math.atan2((b.x - a.x), (b.y - a.y))

    v1h = adx*math.cos(angle)+ady*math.sin(angle)
    v1v = adx*math.sin(angle)-ady*math.cos(angle)
    v2h = bdx*math.cos(angle)+bdy*math.sin(angle)
    v2v = bdx*math.sin(angle)-bdy*math.cos(angle)

    # 충돌방향과 수직성분은 그대로
    # 수평성분은 운동량 보존측과 탄성계수로부터 계산
    e = elasticity  # 탄성계수
    mi = 1  # i 입자의 질량
    mj = 1  # j 입자의 질량
    nv1h = (v2h - v1h) * (1 + e) / (mi / mj + 1) + v1h
    nv2h = (v1h - v2h) * (1 + e) / (mj / mi + 1) + v2h

    # 속도의 수평, 수직 성분을 화면상 x, y 성분으로 수정
    b.dx = nv2h * math.cos(angle) + v2v * math.sin(angle)
    b.dy = (nv2h * math.sin(angle) - v2v * math.cos(angle)) // 2


def collides_distance(a, b):
    ax,ay = a.pos
    bx,by = b.pos
    distance_sqrt = (ax - bx) ** 2 + (ay - by) ** 2
    radius_sum = a.radius + b.radius
    return distance_sqrt < radius_sum ** 2

def check_collision(player1, player2, ball):

    if collides_distance(player1, ball):
        data_stream(player1,ball)
        print("충돌1")
    if collides_distance(player2, ball):
        data_stream(player2, ball)
        print("충돌2")

