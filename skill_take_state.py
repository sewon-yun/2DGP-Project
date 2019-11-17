import game_framework
from pico2d import *
import main_state
import room_select_state
from background import Background

name = "SkillTakeState"
image = None
cursor = None
x, y = 0, 0


def enter():
    global background, cursor
    background = Background()
    if image == None:
        cursor = load_image('cursor.png')


def exit():
    global cursor
    del cursor


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(room_select_state)
                room_select_state.x, room_select_state.y = x, y
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y
    pass


def draw():
    clear_canvas()
    background.draw()
    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
