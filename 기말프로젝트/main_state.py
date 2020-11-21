from pico2d import *
import gfw
import ball
import ball_check
import goal
import goal_check
import game_set
from score import Score
from player import Player
from player2 import Player2
from background import Background
from background import Background2

SCORE_TEXT_COLOR = (255, 255, 255)


def enter():
    gfw.world.init(['bg', 'bg2', 'ball','player1', 'player2', 'goal', 'score'])

    bg = Background('bg.jpg')
    gfw.world.add(gfw.layer.bg, bg)
    bg2 = Background2('grass.png')
    gfw.world.add(gfw.layer.bg2, bg2)

    ball.init()
    gfw.world.add(gfw.layer.ball, ball)

    global player1, player2
    player1 = Player()
    gfw.world.add(gfw.layer.player1, player1)
    player2 = Player2()
    gfw.world.add(gfw.layer.player2, player2)

    goal.init()
    gfw.world.add(gfw.layer.goal, goal)

    global score
    score = Score( get_canvas_width() // 2 +40, 580)
    gfw.world.add(gfw.layer.score, score)

    game_set.init()

    global time, font
    time = 0
    font = gfw.font.load(('res/ENCR10B.TTF'), 20)


def exit():
    pass


def update():
    global player1, player2, ball, time
    time += gfw.delta_time
    game_set.update()
    if game_set.game_start == True:
        gfw.world.update()
        ball_check.check_collision(player1, player2, ball)
        check = goal_check.check_collision()
        if check == 1:
            score.score1 += 1
            reset()
        if check == 2:
            score.score2 += 1
            reset()

def reset():
    ball.reset()
    player1.reset()
    player2.reset()



def draw():
    gfw.world.draw()

    global time, font
    font.draw(10, 580, "time: %.1f" % time, SCORE_TEXT_COLOR)

def handle_event(e):

    global player1,player2
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    game_set.handle_event(e)
    if game_set.game_start == True:
        player1.handle_event(e)
        player2.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()
