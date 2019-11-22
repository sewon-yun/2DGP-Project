from mypico2d import *


class Room:
    image = None
    def __init__(self):
        if Room.image == None:
            self.image = load_image('room_box.png')
            self.image_hp_box = load_image('hp_box.png')
            self.image_dark_elf = load_image('darkelf.png')
            self.font = load_font('gothic.ttf', 25)
        self.roomnum = 0
        (self.monster, self.swamp, self.rest, self.electric_current, self.door, self.torch, self.boss, self.corpse,
         self.fair_wind) = False, False, False, False, False, False, False, False, False
        self.x, self.y = 0, 0

    def get_bb(self):
        return self.x - 75, self.y - 75, self.x + 75, self.y + 75

    def draw(self):
        if self.roomnum == 0:
            self.image.clip_draw(0, 0, 100, 100, 225, 122, 150, 150)
            self.font.draw(185, 170, '현재 방', (255, 255, 255))
            self.image_hp_box.clip_draw(0, 0, 200, 100, 450, 125, 250, 150)
            self.image_dark_elf.clip_draw(0, 0, 800, 800, 75, 125, 150, 150)
            self.font.draw(150, 275, '두 곳 중 이동할 곳을 고르시오', (255, 255, 255))
        elif self.roomnum == 1:
            self.image.clip_draw(0, 0, 100, 100, 155, 400, 150, 150)
        elif self.roomnum == 2:
            self.image.clip_draw(0, 0, 100, 100, 455, 400, 150, 150)
        elif 3 <= self.roomnum <= 6:
            self.image.clip_draw(0, 0, 100, 100, 75 + 150 * (self.roomnum - 3), 575, 150, 150)
        if self.monster:
            self.font.draw(self.x - 20, self.y, '마물', (255, 255, 255))
