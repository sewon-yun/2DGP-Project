import game_framework
from pico2d import *
import main_state

name = "RoomSelectState"
image = None


def enter():
    pass


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass




def draw():
    clear_canvas()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
