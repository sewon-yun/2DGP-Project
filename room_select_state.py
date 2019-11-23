import game_framework
from mypico2d import *
import battle_state
from room import Room
from background import Background
from cursor import Cursor

import random
import game_data

save_num = 0
name = "RoomSelectState"
cursor = None
font = None
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
    ZERO: [225, 100], FIRST: [155, 400], SECOND: [455, 400],
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
    battle_state.monster.name = game_data.monster_table[pick][0] * level
    battle_state.monster.hp = game_data.monster_table[pick][1] * level
    battle_state.monster.maxhp = game_data.monster_table[pick][1] * level
    battle_state.monster.barrior = game_data.monster_table[pick][2] * level
    battle_state.monster.shield = game_data.monster_table[pick][3] * level
    battle_state.monster.attack_damage = game_data.monster_table[pick][4] * level
    battle_state.monster.critical_chance = game_data.monster_table[pick][5] * level
    battle_state.monster.critical_damage = game_data.monster_table[pick][6] * level
    battle_state.monster.experience = game_data.monster_table[pick][7] * level
    battle_state.monster.isAlive = True


def create_room(n, m):
    global rooms
    for i in range(n, m):
        # elements = self.monster, self.swamp, self.rest, self.electric_current, self.door, self.torch, self.boss,
        # self.corpse,self.fair_wind
        dicision = random.randint(1, 100)
        if dicision <= 70:
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


def move_room(k):
    if k == 1:
        move_room_data(0, 1)
        move_room_data(1, 3)
        move_room_data(2, 4)
    elif k == 2:
        move_room_data(0, 2)
        move_room_data(1, 5)
        move_room_data(2, 6)
    for i in range(3, 7):
        rooms[i].monster = 0
        rooms[i].rest = 0
        rooms[i].swamp = 0
        rooms[i].electric_current = 0
        rooms[i].torch = 0
        rooms[i].element = 0
        rooms[i].fair_wind = 0
        rooms[i].corpse = 0
        rooms[i].door = 0
        rooms[i].boss = 0
    create_room(3, 7)


def move_room_data(a, b):
    rooms[a].monster = rooms[b].monster
    rooms[a].rest = rooms[b].rest
    rooms[a].swamp = rooms[b].swamp
    rooms[a].electric_current = rooms[b].electric_current
    rooms[a].torch = rooms[b].torch
    rooms[a].element = rooms[b].element
    rooms[a].fair_wind = rooms[b].fair_wind
    rooms[a].corpse = rooms[b].corpse
    rooms[a].door = rooms[b].door
    rooms[a].boss = rooms[b].boss


def enter():
    hide_cursor()
    global background, cursor, x, y, isCollide, isBattle, rooms, font, start
    isCollide = False
    isBattle = False
    background = Background()
    cursor = Cursor()
    font = load_font('gothic.ttf', 20)
    cursor.x, cursor.y = x, y
    rooms = [Room() for i in range(7)]
    for i in range(0, 7):
        rooms[i].num = i
        rooms[i].x, rooms[i].y = room_location_table[i][0], room_location_table[i][1]
    if not start:
        create_room(1, 7)
    else:
        rooms = battle_state.rooms


def exit():
    global rooms, cursor
    del rooms, cursor


def handle_events():
    global cursor, start, x, y, rooms, isCollide, isBattle, save_num
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
                if collide(cursor, room) and room.num < 3:
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
                        battle_state.cursor.x, battle_state.cursor.y = x, y
                        move_room(save_num)
                        battle_state.rooms = rooms
                        game_framework.pop_state()
                        game_framework.pop_state()
                    else:
                        start = True
                        move_room(save_num)
                        battle_state.rooms = rooms
                        game_framework.pop_state()
                else:
                    move_room(save_num)
                isCollide = False


def draw():
    clear_canvas()
    background.draw()
    for room in rooms:
        room.draw()
    if not rooms[0].torch:
        for i in range(4):
            fill_rectangle_rgb(10 + i * 150, 510, 140 + i * 150, 640, 0, 0, 0)
            font.draw(15 + i * 150, 580, '보이지 않는다', (255, 255, 255))
    cursor.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
