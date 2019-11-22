import random
import json
import os

from mypico2d import *

import game_framework
import room_select_state
import skill_take_state

from background import Background
from character import Character
from monster import Monster
from cursor import Cursor
name = "MainState"

x, y = 0, 0

font = None
background = None
character = None
monster = None
cursor = None
hp_box = None
turn = 0


def enter():
    global background, character, monster, cursor, hp_box, turn
    cursor = Cursor()
    if hp_box == None:
        hp_box = load_image('hp_box.png')
    background = Background()
    character = Character()
    monster = Monster()
    turn = 0


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
            if event.type == SDL_MOUSEBUTTONDOWN and (5 <= x <= 115 and 70 <= y <= 170):
                if character.isAlive:
                    character.attack(character, monster)
                    turn += 1


def update():
    global turn
    character.update()
    if turn % 2 == 1:
        if monster.isAlive:
            monster.attack(monster, character)
            turn += 1
        else:
            turn = 0
            # 화면 전환
            skill_take_state.x, skill_take_state.y = x, y
            game_framework.push_state(skill_take_state)
    pass


def draw():
    clear_canvas()
    background.draw()
    hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
    hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
    character.draw()
    monster.draw()
    cursor.draw()
    update_canvas()
