import random
import json
import os

from mypico2d import *

import game_framework
import room_select_state
import skill_take_state
import victory_state

from background import Background
from character import Character
from monster import Monster
from cursor import Cursor
from room import Room

name = "BattleState"

x, y = 0, 0

font = None
background = None
character = None
monster = None
cursor = None
hp_box = None
rooms = None
turn = 0
count = 0
floor = 1
floor_prograss = 0
delay_time = 0.0

def enter():
    global background, character, monster, cursor, hp_box, turn, rooms
    cursor = Cursor()
    rooms = [Room() for i in range(7)]
    if hp_box == None:
        hp_box = load_image('hp_box.png')
    background = Background()
    character = Character()
    monster = Monster()
    turn = 0
    game_framework.push_state(room_select_state)


def exit():
    global background, cursor, character, monster, hp_box
    del background, cursor, character, monster, hp_box


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y, cursor, turn
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - 1 - event.y
            cursor.x, cursor.y = x, y
        elif turn % 2 == 0:
            for i in range(5):
                if event.type == SDL_MOUSEBUTTONDOWN and (5 + (i * 120) <= x <= 115 + (i * 120) and 70 <= y <= 170) \
                        and character.skills[i].isExist and character.isAlive:
                    if character.skills[i].current_cooldown == 0:
                        character.skills[i].isActive = True
                        if character.skills[i].kinds == 0:
                            character.attack(character, monster)
                        else:
                            character.heal()
                        if rooms[0].fair_wind:
                            character.skills[i].current_cooldown += 1
                        elif rooms[0].swamp:
                            character.skills[i].current_cooldown += character.skills[i].cooldown + 1
                        else:
                            character.skills[i].current_cooldown += character.skills[i].cooldown
                        turn += 1


def update():
    global turn, count, floor, floor_prograss, delay_time
    character.update()
    if turn % 2 == 1:
        if monster.isAlive:
            if delay_time >= 1.0:
                delay_time = 0.0
                monster.attack(monster, character)
                turn += 1
                for i in range(5):
                    if character.skills[i].current_cooldown:
                        character.skills[i].current_cooldown -= 1
            else:
                delay_time += game_framework.frame_time
        else:
            if delay_time >= 1.0:
                delay_time = 0.0
                turn += 1
                for i in range(5):
                    if character.skills[i].current_cooldown:
                        character.skills[i].current_cooldown -= 1
                # 화면 전환
                if rooms[0].rest:
                    character.hp = character.maxhp
                if rooms[0].box:
                    count += 1
                if rooms[0].boss:
                    floor += 1
                    floor_prograss = 0
                    if floor == 6:
                        game_framework.change_state(victory_state)
                        game_framework.quit()
                skill_take_state.x, skill_take_state.y = x, y
                game_framework.push_state(skill_take_state)
            else:
                delay_time += game_framework.frame_time
                if delay_time == 0.5:
                    character.level_up(0)


def draw():
    clear_canvas()
    background.draw()
    hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
    hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
    character.draw()
    monster.draw()
    cursor.draw()
    update_canvas()


