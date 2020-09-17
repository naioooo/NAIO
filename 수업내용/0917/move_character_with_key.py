from pico2d import *

def handle_events():
      global running
      global dx
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

open_canvas()

grass = load_image('../res/grass.png')
character = load_image('../res/character.png')
dx = 0
x = 800 // 2
running = True
while (running):
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x, 90)
      update_canvas()
      handle_events()
      x += dx * 5
      delay(0.01)

close_canvas()

