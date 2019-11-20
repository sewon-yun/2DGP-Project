from mypico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(300, 400)
