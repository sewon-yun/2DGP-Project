import random
import json
import os

from pico2d import *

import game_framework

from background import Background
from character import Character
from monster import Monster

name = "MainState"

x, y = 0, 0

font = None
background = None
character = None
monster = None
cursor = None
hp_box = None


def enter():
    global background, character, monster, cursor, hp_box
    if cursor == None:
        cursor = load_image('cursor.png')
    if hp_box == None:
        hp_box = load_image('hp_box.png')
    background = Background()
    character = Character()
    monster = Monster()


def exit():
    global background, cursor, character, monster, hp_box
    del background, cursor, character, monster, hp_box


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - 1 - event.y
        # else:
        #      character.handle_event(event)


def update():
    character.update()
    pass


def draw():
    clear_canvas()
    hide_cursor()
    background.draw()
    hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
    hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
    character.draw()
    monster.draw()
    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()






