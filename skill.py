from pico2d import *
import mygame
import character

class Skill:
    def __init__(self):
        self.image_skill_9 = load_image('skill_9.png')
        self.slot = 0
        self.skill_num = 1
        self.cooldown = 0
        self.isExist = False
        self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0
        self.critical_chance, self.accuracy = 0, 0
    def draw(self):
        if self.isExist == True:
            if self.skill_num == 1:
                self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)