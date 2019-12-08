import game_framework
from mypico2d import *

name = "GameOverState"
bgm = None
image = None
game_over = None

def enter():
    global bgm, image
    image = load_image('image\\game_over.png')
    bgm = load_music('sound\\lose_music.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    pass


def exit():
    global bgm, image
    del bgm, game_over


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw():
    clear_canvas()
    image.draw(300, 400)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
