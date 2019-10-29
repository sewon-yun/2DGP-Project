from pico2d import *
import mygame
import character


class Equipment:
    def __init__(self):
        self.maxhp, self.avoidability, self.accuracy, self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0, 0, 0, 0
        self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0
    def draw(self):
        pass
