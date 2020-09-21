from pico2d import *
import helper

WIDTH = 800
HEIGHT = 600

def handle_events():
      global running
      global pos
      global delta
      global done
      global target
      global speed
      events = get_events()
      for event in events:
            if event.type == SDL_QUIT:
                  running = False
            elif event.type == SDL_KEYDOWN:
                  if event.key == SDLK_ESCAPE:
                        running = False                        
            elif event.type == SDL_MOUSEBUTTONDOWN:
                  targetlist.extend([event.x, get_canvas_height() - 1 - event.y])                                 
                  speed += 2
                  delta = helper.delta(pos, target, speed)

                       
      

open_canvas(WIDTH, HEIGHT)

grass = load_image('../res/grass.png')
character = load_image('../res/run_animation.png')

x = 400
y = 100
frame = 0
pos = (400, 100)
delta = (0, 0)
speed = 1
done = False
target = (x, y)
targetlist = [x, y]

running = True
while (running):
      clear_canvas()
      grass.draw(400, 30)
      character.clip_draw(frame * 100, 0, 100, 100, pos[0], pos[1])
      update_canvas()
      handle_events()
      pos, done = helper.move_toward(pos, delta, target)
      
      if delta[0] >= 0 and x >= target[0] or delta[0] <= 0 and x <= target[0]:
        done = True
      if(done == False):
          frame = (frame + 1) % 8
      if(done == True):
          speed = 1
          if(len(targetlist) >= 4):
              del targetlist[:2]         
          target = (targetlist[0], targetlist[1])     
          delta = helper.delta(pos, target, speed)
          
      
      delay(0.01)

close_canvas()

