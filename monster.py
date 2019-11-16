from pico2d import *
import random

image = None


class Monster:
    def __init__(self):
        if image == None:
            self.image_rabbit = load_image('rabbit.png')
            # 이미지 추가
            self.font = load_font('gothic.ttf', 20)
        self.x, self.y = 425, 600
        self.hp, self.maxhp, self.barrior, self.shield, self.level = 100, 100, 0, 0, 1
        self.name = '래빗'
        self.attack_damage = 10
        self.isAlive = True
        self.monster_num = 0
        self.experience = 0

    def draw(self):
        if self.isAlive:
            self.image_rabbit.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0:
            draw_rectangle(50, 610, (self.hp / self.maxhp) * 200 + 50, 640)
        if self.barrior > 0:
            pass
        if self.shield > 0:
            pass
        self.font.draw(50, 675, '%s Lv%3.0f' % (self.name, self.level), (255, 255, 255))
        self.font.draw(100, 625, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))

    @staticmethod
    def attack(monster, character):
        character.hp -= random.randint(80, 120) / 100 * monster.attack_damage
        if character.hp <= 0:
            character.hp = 0
            character.isAlive = False

