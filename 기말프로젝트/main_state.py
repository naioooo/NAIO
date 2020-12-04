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

TIME_TEXT_COLOR = (0, 0, 0)
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


    global time, font,check,DELTA_TIME,GOAL_image,goal_sound
    time = 0
    font = gfw.font.load(('res/NAL Hand.otf'), 50)
    check = 0
    DELTA_TIME = 0
    GOAL_image = gfw.image.load('res/goalll.png')
    goal_sound = load_wav('res/shout.wav')
    goal_sound.set_volume(50)


def exit():
    pass



def update():
    global player1, player2, ball, time, font,check,DELTA_TIME,goal_sound

    game_set.update()

    if game_set.game_start == True:
        if DELTA_TIME % 2 != 1:
            gfw.world.update()
        if check == 0:
            time += gfw.delta_time
        ball_check.check_collision(player1, player2, ball)
        if check == 0:
            check = goal_check.check_collision()
            if check == 1:
                score.score1 += 1
                goal_sound.play()
            if check == 2:
                score.score2 += 1
                goal_sound.play()
        else:
           DELTA_TIME += gfw.delta_time
        if DELTA_TIME >= 2:
            check = 0
            DELTA_TIME = 0
            reset()
        if time >= 90:

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

    global time, font, GOAL_image, check
    font.draw(10, 560, "time: %.0f" % time, TIME_TEXT_COLOR)
    if check != 0:
        GOAL_image.draw(get_canvas_width()//2,get_canvas_height()//2)

def handle_event(e):

    global player1,player2,check
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
