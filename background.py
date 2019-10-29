from pico2d import *
import mygame

class Background:
    def __init__(self):
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(600, 800)