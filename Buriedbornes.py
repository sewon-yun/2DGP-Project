# from pico2d import *
#
# BG_WIDTH, BG_HEIGHT = 600, 800
# i, turn = 0, 0
# discrimination = 0
#
# class Equipment:
#     def __init__(self):
#         self.maxhp, self.avoidability, self.accuracy, self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0, 0, 0, 0
#         self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0
#     def draw(self):
#         pass
#
# class Skill:
#     def __init__(self):
#         self.image_skill_9 = load_image('skill_9.png')
#         self.font = load_font('gothic.ttf', 20)
#         self.cooldown_font = load_font('gothic.ttf', 45)
#         self.slot = 0
#         self.skill_num = 1
#         self.cooldown = 0
#         self.isExist = False
#         self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0
#         self.critical_chance, self.accuracy = 0, 0
#     def draw(self):
#         if self.isExist == True:
#             if self.skill_num == 1:
#                 self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)
#                 self.font.draw(10, 55, '그림자 사격', (255, 255, 255))
#                 if self.cooldown > 0:
#                     self.cooldown_font.draw(20, 120, '%3.0f'%self.cooldown, (255, 255, 255))
#
#
# class Character:
#     global discrimination, i
#     def __init__(self):
#         if discrimination == 0:
#             self.image_dark_elf = load_image('darkelf.png')
#         elif discrimination == 1:
#             self.image_fairy = load_image('fairy.png')
#         elif discrimination == 2:
#             self.image_duelist = load_image('duelist.png')
#         elif discrimination == 3:
#             self.image_grave_robber = load_image('grave robber.png')
#         elif discrimination == 4:
#             self.image_vampire = load_image('vampire.png')
#         elif discrimination == 5:
#             self.image_witch = load_image('witch.png')
#         self.font = load_font('gothic.ttf', 20)
#         self.x, self.y, self.experience = 150, 200, 0
#         self.avoidability, self.accuracy, self.critical_chance, self.penetration, self.critical_damage = 0, 0, 0, 0, 0
#         self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 0, 0, 0, 0
#         self.maxhp, self.hp, self.shield, self.barrior, self.level = 0, 0, 0, 0, 1
#         self.isAlive = False
#         self.weapon = Equipment()
#         self.armor = Equipment()
#         self.accessory = Equipment()
#         self.skills = [Skill() for i in range(5)]
#         self.skills[0].isExist = True
#         self.skills[0].strength = 2
#
#     def draw(self):
#         if self.isAlive == True:
#             if discrimination == 0:
#                 self.image_dark_elf.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#             elif discrimination == 1:
#                 self.image_fairy.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#             elif discrimination == 2:
#                 self.image_duelist.clip_draw(0, 0, 900, 1200, self.x, self.y, 300, 400)
#             elif discrimination == 3:
#                 self.image_grave_robber.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#             elif discrimination == 4:
#                 self.image_vampire.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#             elif discrimination == 5:
#                 self.image_witch.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#         if (self.hp / self.maxhp) > 0:
#             draw_rectangle(350, 210, (self.hp / self.maxhp) * 200 + 350, 240)
#         if self.barrior > 0:
#             pass
#         if self.shield > 0:
#             pass
#         self.font.draw(350, 275, 'Lv%3.0f' %self.level, (255, 255, 255))
#         self.skills[0].draw()
#     def update(self):
#         # self.maxhp = self.armor.maxhp + self.weapon.maxhp + self.accessory.maxhp
#         # self.strength = self.armor.strength + self.weapon.strength + self.accessory.strength
#         if self.experience >= 1:
#             self.level += 1
#             self.experience -= 1
#     @staticmethod
#     def attack(character, monster):
#         global turn
#         monster.hp -= character.strength * character.skills[0].strength
#         character.skills[0].cooldown += 1
#         if monster.hp <= 0:
#             monster.isAlive = False
#             character.experience += monster.experience
#         turn += 1
#
# class Monster:
#     def __init__(self):
#         self.image_rabbit = load_image('rabbit.png')
#         self.font = load_font('gothic.ttf', 20)
#         self.x, self.y = 425, 600
#         self.hp, self.maxhp, self.barrior, self.shield, self.level = 0, 0, 0, 0, 1
#         self.attack_damage = 0
#         self.isAlive = False
#         self.monster_num = 0
#         self.experience = 0
#     def draw(self):
#         if self.isAlive:
#             self.image_rabbit.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
#         if (self.hp / self.maxhp) > 0:
#             draw_rectangle(50, 610, (self.hp / self.maxhp) * 200 + 50, 640)
#         if self.barrior > 0:
#             pass
#         if self.shield > 0:
#             pass
#         self.font.draw(50, 675, 'Lv%3.0f' % self.level, (255, 255, 255))
#     @staticmethod
#     def attack(monster, character):
#         global turn
#         character.hp -= monster.attack_damage
#         if character.hp <= 0:
#             character.isAlive = False
#         if character.skills[0].cooldown > 0:
#             character.skills[0].cooldown -= 1
#         turn += 1
#
#
# def handle_events():
#     global running
#     global x, y
#     global turn
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False
#         elif event.type == SDL_MOUSEMOTION:
#             x, y = event.x, BG_HEIGHT - 1 - event.y
#         elif turn % 2 == 0:
#             if event.type == SDL_MOUSEBUTTONDOWN and (5 <= x <= 115 and 70 <= y <= 170):
#                 character.attack(character, monster)
#
#
#
# open_canvas(BG_WIDTH, BG_HEIGHT)
#
# background = load_image('background.png')
# cursor = load_image('cursor.png')
# hp_box = load_image('hp_box.png')
#
# hide_cursor()
# running = True
#
# i = 0
# timer = 0
# character = Character()
# character.hp, character.maxhp, character.strength = 100, 100, 10
# character.isAlive = True
# monster = Monster()
# monster.hp, monster.maxhp = 100, 100
# monster.attack_damage = 8
# monster.experience = 1
# monster.isAlive = True
#
# x, y = BG_WIDTH // 2, BG_HEIGHT // 2
#
# # main
# while running:
#     handle_events()
#     clear_canvas()
#     background.draw(BG_WIDTH // 2, BG_HEIGHT // 2)
#     # for skill in character.skills:
#     #     character.skill.draw()
#     hp_box.clip_draw(0, 0, 200, 100, 450, 250, 250, 125)
#     hp_box.clip_draw(0, 0, 200, 100, 150, 650, 250, 125)
#     monster.draw()
#     character.draw()
#     if timer == 0:
#         if turn % 2 == 0:
#             handle_events()
#         else:
#             if monster.isAlive == True:
#                 monster.attack(monster, character)
#
#     cursor.clip_draw(0, 0, 39, 37, x + 10, y - 10, 30, 30)
#     if timer == 0:
#         timer = 100
#         character.update()
#     else:
#         timer -= 1
#     update_canvas()
#     delay(0.01)
#
# close_canvas()