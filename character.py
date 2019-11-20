from mypico2d import *
import random


image = None




class Equipment:
    def __init__(self):
        (self.maxhp, self.avoidability, self.accuracy,
         self.strength, self.dexerity, self.magic, self.faith, self.power) = 50, 0, 0, 5, 0, 0, 0, 0
        self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0
        self.lifesteal = 0

    def draw(self):
        pass


class Skill:
    def __init__(self):
        if image == None:
            self.image_skill_9 = load_image('skill_9.png')
            self.font = load_font('gothic.ttf', 20)
        self.slot = 0
        self.skill_num = 1
        self.cooldown = 0
        self.name = '그림자 사격'
        self.isExist = False
        self.strength, self.dexerity, self.magic, self.faith, self.power = 2, 0, 0, 0, 0
        self.critical_chance, self.accuracy = 0, 0

    def draw(self):
        self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)
        self.font.draw(self.slot + 10, 55, '%s' % self.name, (255, 255, 255))


class Character:
    def __init__(self):
        if image == None:
            self.image_dark_elf = load_image('darkelf.png')
            self.font = load_font('gothic.ttf', 20)
            self.font_size_15 = load_font('gothic.ttf', 15)
            self.font_size_18 = load_font('gothic.ttf', 18)
        self.x, self.y, self.experience = 150, 200, 0
        self.avoidability, self.accuracy, self.critical_chance, self.penetration, self.critical_damage = 0, 0, 10, 0, 2
        self.strength, self.dexerity, self.magic, self.faith, self.power, self.lifesteal = 10, 0, 0, 0, 0, 0
        self.maxhp, self.hp, self.shield, self.barrior, self.startbarrior, self.level = 0, 150, 0, 0, 1, 1
        self.name = '다크엘프'
        self.isAlive = True
        self.weapon = Equipment()
        self.armor = Equipment()
        self.accessory = Equipment()
        self.skills = Skill()

    def draw(self):
        if self.isAlive:
            self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0 and self.maxhp != 0:
            draw_rectangle(350, 210, 550, 240)
            fill_rectangle(350, 210, (self.hp / self.maxhp) * 200 + 350, 240)
        if self.barrior > 0:
            draw_rectangle_rgb(350, 210, 550, 240, 255, 255, 0)
            pass
        if self.shield > 0:
            pass
        self.font.draw(350, 275, '%s Lv%3.0f' % (self.name, self.level), (255, 255, 255))
        if self.maxhp < 1000 and self.barrior < 1000:
            if self.barrior > 0:
                self.font.draw(390, 225, '%3.0f / %3.0f + %1.0f' % (self.hp, self.maxhp, self.barrior), (255, 255, 0))
                self.font.draw(390, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
            else:
                self.font.draw(400, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
        else:
            if self.barrior > 0:
                self.font_size_15.draw(370, 225, '%3.0f / %3.0f + %1.0f' % (self.hp, self.maxhp, self.barrior), (255, 255, 0))
                self.font_size_15.draw(370, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
            else:
                self.font_size_18.draw(390, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
        self.skills.draw()

    def update(self):
        self.maxhp = self.armor.maxhp + self.weapon.maxhp + self.accessory.maxhp
        self.strength = self.armor.strength + self.weapon.strength + self.accessory.strength

    @staticmethod
    def attack(character, monster):
        if random.randint(1, 100) <= character.critical_chance:
            monster.hp -= character.critical_damage * character.strength * character.skills.strength
        else:
            monster.hp -= random.randint(80, 120) / 100 * character.strength * character.skills.strength
        if monster.hp <= 0:
            monster.hp = 0
            monster.isAlive = False


