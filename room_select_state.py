import game_framework
from mypico2d import *
import main_state
from room import Room
from background import Background
from cursor import Cursor

import random
import game_data

name = "RoomSelectState"
cursor = None
play_turn = 0
floor_prograss = 0
start = False
rooms = []
background = None
isCollide = False
isBattle = False
x, y = 0, 0
(ZERO, FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH) = range(7)
room_location_table = {
    ZERO: [255, 122], FIRST: [155, 400], SECOND: [455, 400],
    THIRD: [75, 575], FOURTH: [225, 575], FIFTH: [375, 575], SIXTH: [525, 575]
}

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


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


def create_room(n, m):
    global rooms
    for i in range(n, m):
        rooms[i].num = i
        rooms[i].x, rooms[i].y = room_location_table[i][0], room_location_table[i][1]
        # elements = self.monster, self.swamp, self.rest, self.electric_current, self.door, self.torch, self.boss,
        # self.corpse,self.fair_wind
        dicision = random.randint(1, 100)
        if dicision <= 60:
            rooms[i].monster = 1
            rooms[i].element += 1
        dicision = random.randint(1, 100)
        if dicision <= 20:
            rooms[i].rest = rooms[i].element + 1
            rooms[i].element += 1
        dicision = random.randint(1, 100)
        if dicision <= 30:
            rooms[i].torch = rooms[i].element + 1
            rooms[i].element += 1


def save_room(i):
    if i == 1:
        rooms[0], rooms[1], rooms[2] = rooms[1], rooms[3], rooms[4]
        for i in range(3):
            rooms[i].num = i
            rooms[i].x, rooms[i].y = room_location_table[i][0], room_location_table[i][1]
    elif i == 2:

        for i in range(3):
            rooms[i].num = i
            rooms[i].x, rooms[i].y = room_location_table[i][0], room_location_table[i][1]


def enter():
    hide_cursor()
    global background, cursor, x, y, isCollide, isBattle, rooms
    isCollide = False
    isBattle = False
    background = Background()
    cursor = Cursor()
    cursor.x, cursor.y = x, y
    rooms = [Room() for i in range(7)]
    create_room(1, 7)



def exit():
    global rooms, cursor
    del rooms, cursor


def handle_events():
    global cursor, start, x, y, rooms, isCollide, isBattle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION and not isBattle:
            x, y = event.x, 800 - 1 - event.y
            cursor.x, cursor.y = x, y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            for room in rooms:
                if collide(cursor, room):
                    if room.num < 3:
                        if room.monster and start:
                            create_monster()
                            isBattle = True
                        elif room.monster and not start:
                            isBattle = True
                        isCollide = True
                        save_num = room.num
            if isCollide:
                if isBattle:
                    if start:
                        main_state.cursor.x, main_state.cursor.y = x, y
                        game_framework.pop_state()
                        game_framework.pop_state()
                    else:
                        start = True
                        game_framework.change_state(main_state)
                else:
                    save_room(save_num)
                    create_room(3, 7)


def draw():
    clear_canvas()
    background.draw()
    for room in rooms:
        room.draw()
    cursor.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
