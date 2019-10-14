from pico2d import *

BG_WIDTH, BG_HEIGHT = 600, 800

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, BG_HEIGHT - 1 - event.y
        # elif event.type == SDL_MOUSEBUTTONDOWN:
        #     running = True
    pass



open_canvas(BG_WIDTH, BG_HEIGHT)

background = load_image('background.png')
monster_rabbit = load_image('rabbit.png')
character_darkelf = load_image('darkelf.png')
cursor = load_image('cursor.png')
hp_box = load_image('hp_box.png')
skill_9 = load_image('skill_9.png')

hide_cursor()
running = True

turn = 0

x, y = BG_WIDTH // 2, BG_HEIGHT // 2

while running:
    clear_canvas()
    background.draw(BG_WIDTH // 2, BG_HEIGHT // 2)
    character_darkelf.clip_draw(0, 0, 800, 800, 200, 200, 300, 300)
    background.clip_draw(0, 0, 600, 200, 0, 120, 1200, 105)
    monster_rabbit.clip_draw(0, 0, 800, 800, 425, 600, 300, 300)
    hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
    hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
    skill_9.clip_draw(200, 300, 60, 50, 60, 120, 110, 100)
    skill_9.clip_draw(200, 300, 60, 50, 180, 120, 110, 100)
    skill_9.clip_draw(200, 300, 60, 50, 300, 120, 110, 100)
    skill_9.clip_draw(200, 300, 60, 50, 420, 120, 110, 100)
    skill_9.clip_draw(200, 300, 60, 50, 540, 120, 110, 100)
    draw_rectangle(350, 210, 550, 240)
    draw_rectangle(50, 610, 250, 640)

    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()

    handle_events()
    delay(0.01)

close_canvas()