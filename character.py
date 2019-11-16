from pico2d import *

image = None


class Equipment:
    def __init__(self):
        (self.maxhp, self.avoidability, self.accuracy,
         self.strength, self.dexerity, self.magic, self.faith, self.power) = 50, 0, 0, 0, 0, 0, 0, 0
        self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0

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
        self.isExist = False
        self.strength, self.dexerity, self.magic, self.faith, self.power = 2, 0, 0, 0, 0
        self.critical_chance, self.accuracy = 0, 0

    def draw(self):
        self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)
        self.font.draw(10, 55, '그림자 사격', (255, 255, 255))


class Character:
    def __init__(self):
        if image == None:
            self.image_dark_elf = load_image('darkelf.png')
            self.font = load_font('gothic.ttf', 20)
        self.x, self.y, self.experience = 150, 200, 0
        self.avoidability, self.accuracy, self.critical_chance, self.penetration, self.critical_damage = 0, 0, 0, 0, 0
        self.strength, self.dexerity, self.magic, self.faith, self.power = 10, 0, 0, 0, 0
        self.maxhp, self.hp, self.shield, self.barrior, self.level = 0, 100, 0, 0, 1
        self.isAlive = True
        self.weapon = Equipment()
        self.armor = Equipment()
        self.accessory = Equipment()
        self.skills = Skill()

    def draw(self):
        if self.isAlive:
            self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0 and self.maxhp != 0:
            draw_rectangle(350, 210, (self.hp / self.maxhp) * 200 + 350, 240)
        if self.barrior > 0:
            pass
        if self.shield > 0:
            pass
        self.font.draw(350, 275, 'Lv%3.0f' % self.level, (255, 255, 255))
        self.skills.draw()

    def update(self):
        self.maxhp = self.armor.maxhp + self.weapon.maxhp + self.accessory.maxhp
        # self.strength = self.armor.strength + self.weapon.strength + self.accessory.strength

    @staticmethod
    def attack(character, monster):
        monster.hp -= character.strength * character.skills.strength
        if monster.hp <= 0:
            monster.isAlive = False


