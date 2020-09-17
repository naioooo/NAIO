from pico2d import *

WIDTH = 800
HEIGHT = 600

def handle_events():
      global running
      global dx
      global x, y
      global HEIGHT
      events = get_events()
      for event in events:
           if event.type == SDL_QUIT:
                  running = False
           elif event.type == SDL_KEYDOWN:
                 if event.key == SDLK_RIGHT:
                       dx += 1
                 elif event.key == SDLK_LEFT:
                       dx -= 1
                 elif event.key == SDLK_ESCAPE:
                       running = False
           elif event.type == SDL_KEYUP:
                 if event.key == SDLK_RIGHT:
                       dx -= 1
                 elif event.key == SDLK_LEFT:
                       dx += 1
           elif event.type == SDL_MOUSEMOTION:
                 x = event.x
                 y = HEIGHT - 1 - event.y
                 

open_canvas(WIDTH, HEIGHT)

grass = load_image('../res/grass.png')
character = load_image('../res/character.png')
dx = 0
x = 800 // 2
y = 100
running = True
while (running):
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x, y)
      update_canvas()
      handle_events()
      x += dx * 5
      delay(0.01)

close_canvas()

