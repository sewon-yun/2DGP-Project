from mypico2d import *
import random

image = None

(RABBIT, SAMURAI, PROPHET, ROCK, TRENT, DURAHAN, CYCLOPS, BUDYFUCKER, ANCIENT) = range(9)

class Monster:
    def __init__(self):
        if image == None:
            self.image_rabbit = load_image('rabbit.png')
            self.image_samurai = load_image('samurai.png')
            self.image_prophet = load_image('prophet.png')
            self.image_rock = load_image('self-destructrock.png')
            self.image_trent = load_image('trent.png')
            self.image_durahan = load_image('durahan.png')
            self.image_cyclops = load_image('cyclops.png')
            self.image_budyfucker = load_image('budyfucker.png')
            self.image_ancient = load_image('ancient.png')
            self.font = load_font('gothic.ttf', 20)
        self.x, self.y = 425, 600
        self.hp, self.maxhp, self.barrior, self.shield, self.level = 100, 100, 0, 0, 1
        self.name = '래빗'
        self.attack_damage, critical_chance, critical_damage = 10, 0, 0
        self.isAlive = True
        self.experience = 0

    def draw(self):
        if self.isAlive:
            if self.name == '래빗':
                self.image_rabbit.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '사무라이':
                self.image_samurai.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '예언가':
                self.image_prophet.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '바위':
                self.image_rock.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '트렌트':
                self.image_trent.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '듀라한':
                self.image_durahan.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '외눈박이':
                self.image_cyclops.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '고문관':
                self.image_budyfucker.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '고대의 것':
                self.image_ancient.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0:
            draw_rectangle(50, 610, 250, 640)
            fill_rectangle(50, 610, (self.hp / self.maxhp) * 200 + 50, 640)
        if self.barrior > 0:
            draw_rectangle_rgb(50, 610, 250, 640, 255, 255, 0)
        if self.shield > 0:
            draw_rectangle_rgb(50, 610, 250, 640, 0, 255, 0)
        self.font.draw(50, 675, '%s Lv%3.0f' % (self.name, self.level), (255, 255, 255))
        self.font.draw(100, 625, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))

    @staticmethod
    def attack(monster, character):
        if character.barrior > 0:
            character.barrior -= random.randint(80, 120) / 100 * monster.attack_damage
            if character.barrior < 0:
                character.hp += character.barrior
        else:
            character.hp -= random.randint(80, 120) / 100 * monster.attack_damage
        if character.hp <= 0:
            character.hp = 0
            character.isAlive = False
