from pico2d import *
import monster
import equipment
import skill
import main_state

x = 0
y = 0
turn = 0
i = 0

class Character:
    def __init__(self):
        self.image_dark_elf = load_image('darkelf.png')
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
        global i
        if self.isAlive:
            self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
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
    # def attack(character, monster):
    #     global turn
    #     monster.hp -= character.strength * character.skills[0].strength
    #     if monster.hp <= 0:
    #         monster.isAlive = False
    #         character.experience += monster.experience
    #     turn += 1

    def handle_events(self, event):
        global x, y
        global turn
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y
            # elif turn % 2 == 0:
            #     if event.type == SDL_MOUSEBUTTONDOWN and (5 <= x <= 115 and 70 <= y <= 170):
            #         self.attack(self, monster)