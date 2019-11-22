import random
from mypico2d import *
import game_framework


class Cursor:
    image = None
    def __init__(self):
        if Cursor.image == None:
            self.image = load_image('game_cursor.png')
        self.x, self.y = 0, 0

    def get_bb(self):
        return self.x - 1, self.y - 1, self.x + 1, self.y + 1

    def draw(self):
        self.image.clip_draw(0, 0, 39, 37, self.x + 10, self.y - 10, 30, 30)

    def update(self):
        pass
