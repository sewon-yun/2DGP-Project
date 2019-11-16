import game_framework
from pico2d import *
import main_state
from room import Room
from background import Background

name = "RoomSelectState"
image = None
cursor = None
x, y = 0, 0


def enter():
    global room, background, cursor
    room = Room()
    background = Background()
    if image == None:
        cursor = load_image('cursor.png')
    pass


def exit():
    global room, cursor
    del room, cursor


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
                game_framework.pop_state()
                # 몬스터 테이블 구현 후 값 삽입
                main_state.monster.isAlive = True
                main_state.monster.hp = 100
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y
    pass


def draw():
    clear_canvas()
    background.draw()
    room.draw()
    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
