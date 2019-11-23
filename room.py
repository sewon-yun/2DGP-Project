from mypico2d import *


class Room:
    image = None
    def __init__(self):
        if Room.image == None:
            self.image = load_image('room_box.png')
            self.image_hp_box = load_image('hp_box.png')
            self.image_dark_elf = load_image('darkelf.png')
            self.image_monster_event = load_image('skill_10.png')
            self.image_element = load_image('skill_11.png')
            self.font = load_font('gothic.ttf', 25)
            self.font_size_18 = load_font('gothic.ttf', 18)
        self.element = 0
        self.num = 0
        self.location = 0
        (self.monster, self.swamp, self.rest, self.electric_current, self.door, self.torch, self.boss, self.corpse,
         self.fair_wind) = 0, 0, 0, 0, 0, 0, 0, 0, 0
        self.x, self.y = 0, 0

    def get_bb(self):
        return self.x - 75, self.y - 75, self.x + 75, self.y + 75

    def draw(self):
        if self.num == 0:
            self.image.clip_draw(0, 0, 100, 100, 225, 122, 150, 150)
            self.font.draw(185, 170, '현재 방', (255, 255, 255))
            self.image_hp_box.clip_draw(0, 0, 200, 100, 450, 125, 250, 150)
            self.image_dark_elf.clip_draw(0, 0, 800, 800, 75, 125, 150, 150)
            self.font.draw(150, 275, '두 곳 중 이동할 곳을 고르시오', (255, 255, 255))
        elif self.num == 1:
            self.image.clip_draw(0, 0, 100, 100, 155, 400, 150, 150)
        elif self.num == 2:
            self.image.clip_draw(0, 0, 100, 100, 455, 400, 150, 150)
        elif 3 <= self.num <= 6:
            self.image.clip_draw(0, 0, 100, 100, 75 + 150 * (self.num - 3), 575, 150, 150)
        if self.monster:
            self.image_monster_event.clip_draw(270, 210, 60, 55, self.x - 25, self.y + 25, 60, 60)
            self.font_size_18.draw(self.x - 45, self.y + 25, '마물', (255, 255, 255))
        if self.rest:
            self.image_element.clip_draw(200, 130, 60, 55, self.x - 25 + (self.rest - 1) * 60, self.y + 25, 60, 60)
            self.font_size_18.draw(self.x - 45 + (self.rest - 1) * 60, self.y + 25, '휴식', (255, 255, 255))

