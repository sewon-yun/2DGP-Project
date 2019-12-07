import game_framework
from mypico2d import *
from cursor import Cursor
from background import Background

import battle_state


name = "VictoryState"
bgm = None
image = None
cursor = None
background = None


def enter():
    global bgm, image, cursor, background
    image = load_image('victory.png')
    bgm = load_music('victory_music.mp3')
    background = Background()
    cursor = Cursor()
    bgm.set_volume(64)
    bgm.repeat_play()
    hide_cursor()
    pass


def exit():
    global bgm, image
    del bgm, image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            cursor.x, cursor.y = event.x, 800 - 1 - event.y
            print(cursor.x, cursor.y)
        elif event.type == SDL_MOUSEBUTTONDOWN and 150 < cursor.x < 450 and 75 < cursor.y < 175:
            game_framework.change_state(battle_state)



def draw():
    clear_canvas()
    background.draw()
    image.draw(300, 400)
    cursor.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
