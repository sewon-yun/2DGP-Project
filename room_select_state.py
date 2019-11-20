import game_framework
from mypico2d import *
import main_state
from room import Room
from background import Background
import random
import game_data

name = "RoomSelectState"
image = None
cursor = None
play_turn = 0
floor_prograss = 0
start = False

x, y = 0, 0


def create_monster():
    # list = [name, hp, barrior, shield, attack_damage, critical_chance, critical_damage, experience]
    #        [ 0     1     2        3          4               5                 6             7    ]
    global play_turn
    level = int(play_turn / 10) + 1
    pick = random.randint(0, 1)
    main_state.monster.name = game_data.monster_table[pick][0] * level
    main_state.monster.hp = game_data.monster_table[pick][1] * level
    main_state.monster.maxhp = game_data.monster_table[pick][1] * level
    main_state.monster.barrior = game_data.monster_table[pick][2] * level
    main_state.monster.shield = game_data.monster_table[pick][3] * level
    main_state.monster.attack_damage = game_data.monster_table[pick][4] * level
    main_state.monster.critical_chance = game_data.monster_table[pick][5] * level
    main_state.monster.critical_damage = game_data.monster_table[pick][6] * level
    main_state.monster.experience = game_data.monster_table[pick][7] * level
    main_state.monster.isAlive = True


def create_room():
    pass


def save_room():
    pass


def enter():
    hide_cursor()
    global room, background, cursor
    room = Room()
    background = Background()
    if image == None:
        cursor = load_image('cursor.png')


def exit():
    global room, cursor
    del room, cursor


def handle_events():
    global x, y, start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                if not start:
                    game_framework.change_state(main_state)
                    start = True
                else:
                    game_framework.pop_state()
                    game_framework.pop_state()
                    # 몬스터 테이블 구현 후 값 삽입
                    create_monster()
                    main_state.x, main_state.y = x, y
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y


def draw():
    clear_canvas()
    background.draw()
    room.draw()
    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()


def update():
    pass

def pause():
    pass


def resume():
    pass
