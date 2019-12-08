from mypico2d import *


class Room:
    image = None

    def __init__(self):
        if Room.image == None:
            self.image = load_image('image\\room_box.png')
            self.image_hp_box = load_image('image\\hp_box.png')
            self.image_dark_elf = load_image('character\\darkelf.png')
            self.image_element = load_image('skill\\skill_4.png')
            self.image_element1 = load_image('skill\\skill_5.png')
            self.image_element2 = load_image('skill\\skill_6.png')
            self.image_element3 = load_image('skill\\skill_10.png')
            self.image_element4 = load_image('skill\\skill_11.png')
            self.image_element5 = load_image('skill\\skill_1.png')
            self.font = load_font('font\\gothic.ttf', 25)
            self.font_size_18 = load_font('font\\gothic.ttf', 18)
        self.element = 0
        self.num = 0
        self.location = 0
        (self.monster, self.swamp, self.rest, self.electric_current, self.door, self.torch, self.boss, self.box,
         self.fair_wind) = 0, 0, 0, 0, 0, 0, 0, 0, 0
        self.x, self.y = 0, 0

    def get_bb(self):
        return self.x - 75, self.y - 75, self.x + 75, self.y + 75

    def draw(self):
        if self.num == 0:
            self.image_dark_elf.clip_draw(0, 0, 800, 800, 75, 125, 150, 150)
            self.image.clip_draw(0, 0, 100, 100, 225, 122, 200, 200)
            self.font.draw(185, 180, '현재 방', (255, 255, 255))
            self.image_hp_box.clip_draw(0, 0, 200, 100, 450, 125, 250, 150)
            self.font.draw(150, 275, '두 곳 중 이동할 곳을 고르시오', (255, 255, 255))

        elif self.num == 1:
            self.image.clip_draw(0, 0, 100, 100, 155, 400, 150, 150)

        elif self.num == 2:
            self.image.clip_draw(0, 0, 100, 100, 455, 400, 150, 150)

        elif 3 <= self.num <= 6:
            self.image.clip_draw(0, 0, 100, 100, 75 + 150 * (self.num - 3), 575, 150, 150)

        if self.door:
            self.image_element2.clip_draw(330, 300, 60, 55, self.x + 3, self.y + 10, 60, 60)
            self.font_size_18.draw(self.x - 10, self.y + 7, '문', (255, 255, 0))
            pass
        else:
            if self.monster:
                self.image_element3.clip_draw(270, 210, 60, 55, self.x - 28, self.y + 35, 60, 60)
                self.font_size_18.draw(self.x - 45, self.y + 25, '마물', (255, 255, 0))

            if self.boss:
                self.image_element1.clip_draw(140, 125, 60, 55, self.x - 28, self.y + 38, 60, 60)
                self.font_size_18.draw(self.x - 45, self.y + 25, '보스', (255, 255, 0))

            if self.rest:
                self.image_element4.clip_draw(200, 125, 60, 55, self.x - 30 + (self.rest - 1) * 60, self.y + 35, 60, 60)
                self.font_size_18.draw(self.x - 45 + (self.rest - 1) * 60, self.y + 25, '휴식', (255, 255, 0))

            if self.torch:
                if self.torch < 3:
                    self.image_element4.clip_draw(329, 125, 60, 55, self.x - 28 + (self.torch - 1) * 60, self.y + 35,
                                                  60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.torch - 1) * 60, self.y + 25, '횃불', (255, 255, 0))
                else:
                    self.image_element4.clip_draw(330, 125, 60, 55, self.x - 28 + (self.torch - 3) * 60, self.y - 30,
                                                  60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.torch - 3) * 60, self.y - 40, '횃불', (255, 255, 0))

            if self.box:
                if self.box < 3:
                    self.image_element4.clip_draw(16, 125, 60, 55, self.x - 28 + (self.box - 1) * 60, self.y + 35, 60,
                                                  60)
                    self.font_size_18.draw(self.x - 45 + (self.box - 1) * 60, self.y + 25, '상자', (255, 255, 0))
                else:
                    self.image_element4.clip_draw(16, 125, 60, 55, self.x - 28 + (self.box - 3) * 60, self.y - 30, 60,
                                                  60)
                    self.font_size_18.draw(self.x - 45 + (self.box - 3) * 60, self.y - 40, '상자', (255, 255, 0))

            if self.swamp:
                if self.swamp < 3:
                    self.image_element.clip_draw(140, 35, 60, 55, self.x - 28 + (self.swamp - 1) * 60, self.y + 37, 60,
                                                 60)
                    self.font_size_18.draw(self.x - 40 + (self.swamp - 1) * 60, self.y + 25, '늪', (255, 255, 0))
                else:
                    self.image_element.clip_draw(140, 35, 60, 55, self.x - 28 + (self.swamp - 3) * 60, self.y - 29, 60,
                                                 60)
                    self.font_size_18.draw(self.x - 40 + (self.swamp - 3) * 60, self.y - 40, '늪', (255, 255, 0))

            if self.fair_wind:
                if self.fair_wind < 3:
                    self.image_element2.clip_draw(80, 125, 60, 55, self.x - 28 + (self.fair_wind - 1) * 60, self.y + 37,
                                                  60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.fair_wind - 1) * 60, self.y + 25, '순풍', (255, 255, 0))
                else:
                    self.image_element2.clip_draw(80, 125, 60, 55, self.x - 28 + (self.fair_wind - 3) * 60, self.y - 27,
                                                  60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.fair_wind - 3) * 60, self.y - 40, '순풍', (255, 255, 0))

            if self.electric_current:
                if self.electric_current < 3:
                    self.image_element5.clip_draw(140, 293, 60, 55, self.x - 28 + (self.electric_current - 1) * 60,
                                                  self.y + 37, 60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.electric_current - 1) * 60, self.y + 25, '전류',
                                           (255, 255, 0))
                else:
                    self.image_element5.clip_draw(141, 293, 60, 55, self.x - 28 + (self.electric_current - 3) * 60,
                                                  self.y - 29, 60, 60)
                    self.font_size_18.draw(self.x - 45 + (self.electric_current - 3) * 60, self.y - 40, '전류',
                                           (255, 255, 0))
