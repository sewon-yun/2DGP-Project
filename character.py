from pico2d import *
import mygame
import monster
import equipment
import skill

class Character:
    global discrimination, i
    def __init__(self):
        if discrimination == 0:
            self.image_dark_elf = load_image('darkelf.png')
        elif discrimination == 1:
            self.image_fairy = load_image('fairy.png')
        elif discrimination == 2:
            self.image_duelist = load_image('duelist.png')
        elif discrimination == 3:
            self.image_grave_robber = load_image('grave robber.png')
        elif discrimination == 4:
            self.image_vampire = load_image('vampire.png')
        elif discrimination == 5:
            self.image_witch = load_image('witch.png')
        self.font = load_font('gothic.ttf', 20)
        self.x, self.y, self.experience = 150, 200, 0
        self.avoidability, self.accuracy, self.critical_chance, self.penetration, self.critical_damage = 0, 0, 0, 0, 0
        self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0
        self.maxhp, self.hp, self.shield, self.barrior, self.level = 0, 0, 0, 0, 1
        self.isAlive = False
        self.weapon = equipment.Equipment()
        self.armor = equipment.Equipment()
        self.accessory = equipment.Equipment()
        self.skills = [skill.Skill() for i in range(5)]
        self.skills[0].isExist = True
        self.skills[0].strength = 2

    def draw(self):
        if self.isAlive == True:
            if discrimination == 0:
                self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif discrimination == 1:
                self.image_fairy.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif discrimination == 2:
                self.image_duelist.clip_draw(0, 0, 900, 1200, self.x, self.y, 300, 400)
            elif discrimination == 3:
                self.image_grave_robber.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif discrimination == 4:
                self.image_vampire.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif discrimination == 5:
                self.image_witch.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if (self.hp / self.maxhp) > 0:
            draw_rectangle(350, 210, (self.hp / self.maxhp) * 200 + 350, 240)
        if self.barrior > 0:
            pass
        if self.shield > 0:
            pass
        self.font.draw(350, 275, 'Lv%3.0f' %self.level, (255, 255, 255))
        self.skills[0].draw()
    def update(self):
        self.maxhp = self.armor.maxhp + self.weapon.maxhp + self.accessory.maxhp
        self.strength = self.armor.strength + self.weapon.strength + self.accessory.strength
    @staticmethod
    def attack(character, monster):
        global turn
        monster.hp -= character.strength * character.skills[0].strength
        if monster.hp <= 0:
            monster.isAlive = False
            character.experience += monster.experience
        turn += 1
