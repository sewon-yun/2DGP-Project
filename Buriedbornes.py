from pico2d import *
import random

BG_WIDTH, BG_HEIGHT = 600, 800
class Equipment:
    def __init__(self):
        self.maxhp, self.avoidability, self.accuracy, self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0, 0, 0, 0
        self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0
    def draw(self):
        pass

class Character:
    def __init__(self):
        self.image_dark_elf = load_image('darkelf.png')
        self.image_fairy = load_image('fairy.png')
        self.image_duelist = load_image('duelist.png')
        self.image_grave_robber = load_image('grave robber.png')
        self.image_vampire = load_image('vampire.png')
        self.image_witch = load_image('witch.png')
        self.x, self.y, self.experience = 150, 200, 0
        self.discrimination = random.randint(0, 5)
        self.avoidability, self.accuracy, self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0, 0, 0
        self.maxhp, self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0, 0
        self.weapon = Equipment()
        self.armor = Equipment()
        self.accessory = Equipment()
    def draw(self):
        if self.discrimination == 0:
            self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if self.discrimination == 1:
            self.image_fairy.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if self.discrimination == 2:
            self.image_duelist.clip_draw(0, 0, 900, 1200, self.x, self.y, 300, 400)
        if self.discrimination == 3:
            self.image_grave_robber.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if self.discrimination == 4:
            self.image_vampire.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
        if self.discrimination == 5:
            self.image_witch.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
    def update(self):
        pass
class Skill:
    def __init__(self):
        self.image_skill_9 = load_image('skill_9.png')
        self.slot = 1
        self.skill_num = 1
        self.cooldown = 0
        self.isExist = False
        self.strength, self.dexerity, self.magic, self.faith, self.power, self.critical_chance, self.accuracy = 0, 0, 0, 0, 0, 0, 0
    def draw(self):
        if self.isExist == True:
            self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)


class Monster:
    def __init__(self):
        self.image_rabbit = load_image('rabbit.png')
        self.x, self.y = 425, 600
        self.isAlive = False
        self.monster_num = 0
        self.experence = 0
    def draw(self):
        if self.isAlive:
            self.image_rabbit.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, BG_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass
    pass



open_canvas(BG_WIDTH, BG_HEIGHT)

background = load_image('background.png')
cursor = load_image('cursor.png')
hp_box = load_image('hp_box.png')

hide_cursor()
running = True

turn = 0
i = 0
skills = [Skill() for i in range(5)]

while i < 5:
    skills[i].slot = i
    i += 1
skills[0].isExist = True
character = Character()
monsters = [Monster() for i in range(1)]

monsters[0].isAlive = True

x, y = BG_WIDTH // 2, BG_HEIGHT // 2

while running:
    handle_events()


    clear_canvas()
    background.draw(BG_WIDTH // 2, BG_HEIGHT // 2)
    character.draw()
    for monster in monsters:
        monster.draw()
    background.clip_draw(0, 0, 600, 200, 0, 0, 1200, 120)
    for skill in skills:
        skill.draw()
    hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
    hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
    draw_rectangle(350, 210, 550, 240)
    draw_rectangle(50, 610, 250, 640)

    cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
    update_canvas()

    delay(0.01)

close_canvas()