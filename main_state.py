from pico2d import *
import game_framework
# import equipment
# import skill

from character import Character
from monster import Monster
from background import Background

name = "MainState"

monster = None
character = None
background = None
font = None

def enter():
    global monster, character, background
    monster = Monster()
    character = Character()
    background = Background()

def exit():
    global monster, character, background
    del monster
    del character
    del background

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            pass
            #character.handle_event(event)



def update():
    #character.update()
    pass

def draw():
    clear_canvas()
    background.draw()
    monster.draw()
    character.draw()
    update_canvas()



