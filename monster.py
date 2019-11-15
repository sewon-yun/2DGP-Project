from pico2d import *

class Monster:
    def __init__(self):
        self.image_rabbit = load_image('rabbit.png')
        self.font = load_font('gothic.ttf', 20)
        self.x, self.y = 425, 600
        self.hp, self.maxhp, self.barrior, self.shield, self.level = 100, 100, 0, 0, 1
        self.attack_damage = 0
        self.isAlive = False
        self.monster_num = 0
        self.experience = 0
    def draw(self):
        self.image_rabbit.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0:
            draw_rectangle(50, 610, (self.hp / self.maxhp) * 200 + 50, 640)
        if self.barrior > 0:
            pass
        if self.shield > 0:
            pass
        self.font.draw(50, 675, 'Lv%3.0f' % self.level, (255, 255, 255))