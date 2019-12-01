from mypico2d import *
import random
import game_data
import battle_state

image = None
count = 0

class Equipment:
    def __init__(self):
        self.maxhp, self.strength, self.dexerity, self.magic, self.faith, self.power = 100, 0, 30, 0, 0, 0
        self.shield, self.critical_chance, self.penetration, self.critical_damage, self.barrior = 0, 0, 0, 0, 0
        self.lifesteal = 0

    def draw(self):
        pass


class Skill:
    def __init__(self):
        if image == None:
            self.image_skill_1 = load_image('skill_1.png')
            self.image_skill_7 = load_image('skill_7.png')
            self.image_skill_8 = load_image('skill_8.png')
            self.image_skill_9 = load_image('skill_9.png')
            self.font = load_font('gothic.ttf', 20)
            self.font_size_25 = load_font('gothic.ttf', 25)
            self.cooldown_font = load_font('gothic.ttf', 40)
        self.slot = 0
        self.current_cooldown = 0
        self.cooldown = 1
        self.name = '그림자 사격'
        self.isExist = False
        self.isActive = False
        self.strength, self.dexerity, self.magic, self.faith, self.power = 0, 2, 0, 0, 0
        self.kinds = 0
        self.skill_select = False
        self.skill_pick = False
        self.level = 0

    def draw(self):
        if self.skill_pick:
            if self.name == '그림자 사격':
                self.image_skill_9.clip_draw(200, 300, 60, 50, 450, 350, 110, 100)
                self.font_size_25.draw(390, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '회복':
                self.image_skill_8.clip_draw(80, 213, 60, 50, 450, 350, 110, 100)
                self.font_size_25.draw(420, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '완전 회복' or self.name == '상급 회복':
                self.image_skill_8.clip_draw(80, 213, 60, 50, 450, 350, 110, 100)
                self.font_size_25.draw(395, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '정조준':
                self.image_skill_1.clip_draw(80, 293, 60, 50, 450, 350, 110, 100)
                self.font_size_25.draw(410, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '사격':
                self.image_skill_7.clip_draw(335, 40, 60, 52, 450, 350, 100, 100)
                self.font_size_25.draw(420, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '암습':
                self.image_skill_7.clip_draw(270, 213, 60, 52, 450, 350, 100, 100)
                self.font_size_25.draw(420, 270, '%s' % self.name, (255, 255, 255))
            elif self.name == '응급 처치' or '상처 치료':
                self.image_skill_8.clip_draw(267, 300, 60, 50, 450, 350, 110, 100)
                self.font_size_25.draw(395, 270, '%s' % self.name, (255, 255, 255))
        else:
            if self.level == 0:
                if self.skill_select:
                    if self.name == '그림자 사격':
                        self.image_skill_9.clip_draw(200, 300, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(90, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '회복':
                        self.image_skill_8.clip_draw(80, 213, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(120, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '완전 회복' or self.name == '상급 회복':
                        self.image_skill_8.clip_draw(80, 213, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(95, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '정조준':
                        self.image_skill_1.clip_draw(80, 293, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(110, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '사격':
                        self.image_skill_7.clip_draw(335, 40, 60, 52, 150, 350, 100, 100)
                        self.font_size_25.draw(120, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '암습':
                        self.image_skill_7.clip_draw(270, 213, 60, 52, 150, 350, 100, 100)
                        self.font_size_25.draw(120, 270, '%s' % self.name, (255, 255, 255))
                    elif self.name == '응급 처치' or '상처 치료':
                        self.image_skill_8.clip_draw(267, 300, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(95, 270, '%s' % self.name, (255, 255, 255))
                else:
                    if self.isExist:
                        if self.name == '그림자 사격':
                            self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)
                            self.font.draw(self.slot * 120 + 10, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '회복':
                            self.image_skill_8.clip_draw(80, 213, 60, 50, 66 + self.slot * 120, 120 - 3, 110, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '완전 회복' or self.name == '상급 회복':
                            self.image_skill_8.clip_draw(80, 213, 60, 50, 66 + self.slot * 120, 120 - 3, 110, 100)
                            self.font.draw(self.slot * 120 + 13, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '정조준':
                            self.image_skill_1.clip_draw(80, 293, 60, 50, 64 + self.slot * 120, 120 - 4, 110, 100)
                            self.font.draw(self.slot * 120 + 25, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '사격':
                            self.image_skill_7.clip_draw(335, 40, 60, 52, 61 + self.slot * 120, 120 - 3, 100, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '암습':
                            self.image_skill_7.clip_draw(270, 213, 60, 52, 64 + self.slot * 120, 120 - 3, 100, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s' % self.name, (255, 255, 255))
                        elif self.name == '응급 처치' or '상처 치료':
                            self.image_skill_8.clip_draw(267, 300, 60, 50, 65 + self.slot * 120, 120 - 2, 110, 100)
                            self.font.draw(self.slot * 120 + 15, 55, '%s' % self.name, (255, 255, 255))
                        if self.current_cooldown > 0:
                            fill_rectangle_rgb(18 + self.slot * 120, 75, 102 + self.slot * 120, 160, 20, 20, 20)
                        if 0 < self.current_cooldown < 10:
                            self.cooldown_font.draw(self.slot * 120 + 50, 118, '%1.0f' % self.current_cooldown, (255, 255, 255))
                        if 10 <= self.current_cooldown:
                            self.cooldown_font.draw(self.slot * 120 + 35, 118, '%1.0f' % self.current_cooldown, (255, 255, 255))
            else:
                if self.skill_select:
                    if self.name == '그림자 사격':
                        self.image_skill_9.clip_draw(200, 300, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(90, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '회복':
                        self.image_skill_8.clip_draw(80, 213, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(120, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '완전 회복' or self.name == '상급 회복':
                        self.image_skill_8.clip_draw(80, 213, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(95, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '정조준':
                        self.image_skill_1.clip_draw(80, 293, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(110, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '사격':
                        self.image_skill_7.clip_draw(335, 40, 60, 52, 150, 350, 100, 100)
                        self.font_size_25.draw(120, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '암습':
                        self.image_skill_7.clip_draw(270, 213, 60, 52, 150, 350, 100, 100)
                        self.font_size_25.draw(120, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                    elif self.name == '응급 처치' or '상처 치료':
                        self.image_skill_8.clip_draw(267, 300, 60, 50, 150, 350, 110, 100)
                        self.font_size_25.draw(95, 270, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                else:
                    if self.isExist:
                        if self.name == '그림자 사격':
                            self.image_skill_9.clip_draw(200, 300, 60, 50, 60 + self.slot * 120, 120, 110, 100)
                            self.font.draw(self.slot * 120 + 10, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '회복':
                            self.image_skill_8.clip_draw(80, 213, 60, 50, 66 + self.slot * 120, 120 - 3, 110, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '완전 회복' or self.name == '상급 회복':
                            self.image_skill_8.clip_draw(80, 213, 60, 50, 66 + self.slot * 120, 120 - 3, 110, 100)
                            self.font.draw(self.slot * 120 + 13, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '정조준':
                            self.image_skill_1.clip_draw(80, 293, 60, 50, 64 + self.slot * 120, 120 - 4, 110, 100)
                            self.font.draw(self.slot * 120 + 25, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '사격':
                            self.image_skill_7.clip_draw(335, 40, 60, 52, 61 + self.slot * 120, 120 - 3, 100, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '암습':
                            self.image_skill_7.clip_draw(270, 213, 60, 52, 64 + self.slot * 120, 120 - 3, 100, 100)
                            self.font.draw(self.slot * 120 + 40, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        elif self.name == '응급 처치' or '상처 치료':
                            self.image_skill_8.clip_draw(267, 300, 60, 50, 65 + self.slot * 120, 120 - 2, 110, 100)
                            self.font.draw(self.slot * 120 + 15, 55, '%s+%1.0f' % (self.name, self.level), (255, 255, 255))
                        if self.current_cooldown > 0:
                            fill_rectangle_rgb(18 + self.slot * 120, 75, 102 + self.slot * 120, 160, 20, 20, 20)
                        if 0 < self.current_cooldown < 10:
                            self.cooldown_font.draw(self.slot * 120 + 50, 118, '%1.0f' % self.current_cooldown, (255, 255, 255))
                        if 10 <= self.current_cooldown:
                            self.cooldown_font.draw(self.slot * 120 + 35, 118, '%1.0f' % self.current_cooldown, (255, 255, 255))

    def create(self, pick):
        self.current_cooldown = 0
        self.cooldown = game_data.skill_table[pick][0]
        self.name = game_data.skill_table[pick][1]
        self.strength = game_data.skill_table[pick][2]
        self.dexerity = game_data.skill_table[pick][3]
        self.magic = game_data.skill_table[pick][4]
        self.faith = game_data.skill_table[pick][5]
        self.power = game_data.skill_table[pick][6]
        self.kinds = game_data.skill_table[pick][7]
        self.isExist = True


class Character:
    def __init__(self):
        if image == None:
            self.image_dark_elf = load_image('darkelf.png')
            self.font = load_font('gothic.ttf', 20)
            self.font_size_15 = load_font('gothic.ttf', 15)
            self.font_size_18 = load_font('gothic.ttf', 18)
        self.x, self.y, self.experience = 150, 200, 0
        self.critical_chance, self.penetration, self.critical_damage = 10, 0, 2
        self.strength, self.dexerity, self.magic, self.faith, self.power, self.lifesteal = 0, 10, 0, 0, 0, 0
        self.maxhp, self.hp, self.shield, self.barrior, self.startbarrior, self.level = 0, 300, 0, 0, 1, 1
        self.name = '다크엘프'
        self.isAlive = True
        self.weapon = Equipment()
        self.armor = Equipment()
        self.accessory = Equipment()
        self.skills = [Skill() for i in range(5)]
        for i in range(5):
            self.skills[i].slot = i
        self.skills[0].create(0)
        self.skills[1].create(7)
        self.skills[2].create(2)
        self.skills[3].create(1)
        self.skills[4].create(3)

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
                self.font_size_15.draw(370, 225, '%3.0f / %3.0f + %1.0f' % (self.hp, self.maxhp, self.barrior),
                                       (255, 255, 0))
                self.font_size_15.draw(370, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
            else:
                self.font_size_18.draw(390, 225, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
        for i in range(5):
            self.skills[i].draw()

    def update(self):
        self.maxhp = self.armor.maxhp + self.weapon.maxhp + self.accessory.maxhp
        self.dexerity = self.armor.dexerity + self.weapon.dexerity + self.accessory.dexerity
        self.strength = self.armor.strength + self.weapon.strength + self.accessory.strength
    def level_up(self, n):
        global count
        if self.experience >= game_data.experence_table[self.level]:
            self.level += 1
            count += 1
            print('레벨 업')
            self.level_up(n + 1)
        else:
            battle_state.count += count
            count = 0
            print(battle_state.count)

    @staticmethod
    def attack(character, monster):
        for i in range(5):
            if character.skills[i].isActive:
                if random.randint(1, 100) <= character.critical_chance:
                    monster.hp -= character.critical_damage * (character.strength * character.skills[i].strength +
                                                               character.dexerity * character.skills[i].dexerity +
                                                               character.faith * character.skills[i].faith +
                                                               character.magic * character.skills[i].magic) * \
                                                              (1.1 ** character.skills[i].level)

                else:
                    monster.hp -= random.randint(80, 120) / 100 * (character.strength * character.skills[i].strength +
                                                                   character.dexerity * character.skills[i].dexerity +
                                                                   character.faith * character.skills[i].faith +
                                                                   character.magic * character.skills[i].magic) * \
                                                              (1.1 ** character.skills[i].level)
                if monster.hp <= 0:
                    monster.hp = 0
                    monster.isAlive = False
                    character.experience += monster.experience
                character.skills[i].isActive = False

    def heal(self):
        for i in range(5):
            if self.skills[i].isActive:
                self.hp += self.skills[i].power * self.hp
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
                self.skills[i].isActive = False
