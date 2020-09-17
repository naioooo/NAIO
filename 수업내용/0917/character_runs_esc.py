from pico2d import *

open_canvas()

grass = load_image('../res/grass.png')
character = load_image('../res/character.png')

x = 0
running = True
while (running):
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x, 90)
      update_canvas()
      e = get_events()
      for e in e:
            if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
                  running = False                  
      x = x + 2
      delay(0.01)

close_canvas()

