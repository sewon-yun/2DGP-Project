from mypico2d import *
import random

image = None

(RABBIT, SAMURAI, PROPHET, ROCK, TRENT, DURAHAN, CYCLOPS, BUDYFUCKER, ANCIENT) = range(9)

class Monster:
    def __init__(self):
        if image == None:
            self.image_rabbit = load_image('monster\\rabbit.png')
            self.image_samurai = load_image('monster\\samurai.png')
            self.image_prophet = load_image('monster\\prophet.png')
            self.image_rock = load_image('monster\\self-destructrock.png')
            self.image_trent = load_image('monster\\trent.png')
            self.image_durahan = load_image('monster\\durahan.png')
            self.image_cyclops = load_image('monster\\cyclops.png')
            self.image_budyfucker = load_image('monster\\budyfucker.png')
            self.image_ancient = load_image('monster\\ancient.png')
            self.image_phoenix = load_image('monster\\phoenix.png')
            self.image_vampire = load_image('monster\\vampirelord.png')
            self.image_death = load_image('monster\\death.png')
            self.image_lilith = load_image('monster\\devilqueen.png')
            self.image_concubine = load_image('monster\\bosswife.png')
            self.image_king = load_image('monster\\boss.png')
            self.font = load_font('font\\gothic.ttf', 20)
            self.font_size_15 = load_font('font\\gothic.ttf', 15)
            self.font_size_18 = load_font('font\\gothic.ttf', 18)
            self.death_sound = load_wav('sound\\monster-growl1.wav')
            self.death_sound.set_volume(128)
            self.attack_sound = load_wav('sound\\dart1.wav')
            self.attack_sound.set_volume(32)
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
            elif self.name == '불사조':
                self.image_phoenix.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '뱀파이어 로드':
                self.image_vampire.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '데스':
                self.image_death.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '릴리스':
                self.image_lilith.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '패왕의 첩':
                self.image_concubine.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
            elif self.name == '고대의 패왕':
                self.image_king.clip_draw(0, 0, 800, 800, self.x, self.y, 300, 300)
                pass
        draw_rectangle(50, 610, 250, 640)
        if (self.hp / self.maxhp) > 0:
            fill_rectangle(50, 610, (self.hp / self.maxhp) * 200 + 50, 640)
        if self.barrior > 0:
            draw_rectangle_rgb(50, 610, 250, 640, 255, 255, 0)
        if self.shield > 0:
            draw_rectangle_rgb(50, 610, 250, 640, 0, 255, 0)
        self.font.draw(50, 675, '%s Lv%3.0f' % (self.name, self.level), (255, 255, 255))
        if self.maxhp < 1000 and self.barrior < 1000:
            if self.barrior > 0:
                self.font.draw(90, 625, '%3.0f / %3.0f + %1.0f' % (self.hp, self.maxhp, self.barrior), (255, 255, 0))
                self.font.draw(90, 625, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
            else:
                self.font.draw(100, 625, '%3.0f / %1.0f' % (self.hp, self.maxhp), (255, 255, 255))
        else:
            if self.barrior > 0:
                self.font_size_15.draw(70, 625, '%3.0f / %3.0f + %1.0f' % (self.hp, self.maxhp, self.barrior),
                                       (255, 255, 0))
                self.font_size_15.draw(70, 625, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))
            else:
                self.font_size_18.draw(90, 625, '%3.0f / %3.0f' % (self.hp, self.maxhp), (255, 255, 255))

    @staticmethod
    def attack(monster, character):
        monster.attack_sound.play(1)
        if character.barrior > 0:
            character.barrior -= random.randint(80, 120) / 100 * monster.attack_damage
            if character.barrior < 0:
                character.hp += character.barrior
        else:
            character.hp -= random.randint(80, 120) / 100 * monster.attack_damage
        if character.hp <= 0:
            character.hp = 0
            character.isAlive = False
