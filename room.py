from pico2d import *

image = None


class Room:
    def __init__(self):
        if image == None:
            self.image = load_image('room_box.png')
            self.image_hp_box = load_image('hp_box.png')
            self.image_dark_elf = load_image('darkelf.png')
            self.font = load_font('gothic.ttf', 25)

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, 75, 575, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 225, 575, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 375, 575, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 525, 575, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 155, 400, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 455, 400, 150, 150)
        self.image.clip_draw(0, 0, 100, 100, 225, 122, 150, 150)
        self.image_hp_box.clip_draw(0, 0, 200, 100, 450, 125, 250, 150)
        self.image_dark_elf.clip_draw(0, 0, 800, 800, 75, 125, 150, 150)
        self.font.draw(150, 275, '두 곳 중 이동할 곳을 고르시오', (255, 255, 255))
        self.font.draw(185, 170, '현재 방', (255, 255, 255))