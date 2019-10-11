from pico2d import *

BG_WIDTH, BG_HEIGHT = 600, 800

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(BG_WIDTH, BG_HEIGHT)
background = load_image('background.png')
monster_rabbit = load_image('rabbit.png')
character_darkelf = load_image('darkelf.png')

running = True

x, y = BG_WIDTH // 2, BG_HEIGHT // 2

while running:
    clear_canvas()
    background.draw(BG_WIDTH // 2, BG_HEIGHT // 2)
    character_darkelf.clip_draw(0, 0, 800, 800, 150, 300, 300, 300)
    monster_rabbit.clip_draw(0, 0, 800, 800, 450, 600, 300, 300)
    update_canvas()

    handle_events()
    delay(0.01)

close_canvas()