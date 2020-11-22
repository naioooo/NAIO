from pico2d import *
import gfw
import ball
import ball_check
import goal
import goal_check
import game_set
import end_state1
import end_state2
import end_state3
from score import Score
from player import Player
from player2 import Player2
from background import Background
from background import Background2
from background import HorzScrollBackground

TIME_TEXT_COLOR = (255, 100, 255)
SCORE_TEXT_COLOR = (0, 0, 0)



def enter():
    gfw.world.init(['bg', 'bg2','cloud', 'ball','player1', 'player2', 'goal', 'score'])

    bg = Background('bg.jpg')
    gfw.world.add(gfw.layer.bg, bg)
    bg2 = Background2('grass.jpg')
    gfw.world.add(gfw.layer.bg2, bg2)
    cloud = HorzScrollBackground('clouds2.png')
    cloud.speed = 10
    gfw.world.add(gfw.layer.cloud, cloud)

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
    font = gfw.font.load(('res/NAL Hand.otf'), 50)



def exit():
    pass


def update():
    global player1, player2, ball, time, font

    game_set.update()

    if game_set.game_start == True:
        gfw.world.update()
        time += gfw.delta_time
        ball_check.check_collision(player1, player2, ball)
        check = goal_check.check_collision()
        if check == 1:
            score.score1 += 1
            reset()
        if check == 2:
            score.score2 += 1
            reset()
        if time >= 5:

            game_set.sound.stop()
            game_set.game_start = False
            if  score.display1 > score.display2:
                gfw.push(end_state1)
            elif  score.display1 < score.display2:
                gfw.push(end_state2)
            elif score.display1 == score.display2:
                gfw.push(end_state3)
            game_reset()




def reset():
    ball.reset()
    player1.reset()
    player2.reset()

def game_reset():
    global player1, player2, ball, time
    score.display1 = 0
    score.display2 = 0
    score.score1 = 0
    score.score2 = 0
    reset()
    time = 0

def draw():
    gfw.world.draw()

    global time, font
    font.draw(10, 560, "time: %.1f" % time, TIME_TEXT_COLOR)

def handle_event(e):

    global player1,player2
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_r:
            game_reset()
            game_set.game_start = False
    game_set.handle_event(e)
    if game_set.game_start == True:
        player1.handle_event(e)
        player2.handle_event(e)




def pause():
    pass


def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
