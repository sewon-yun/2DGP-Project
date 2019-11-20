from mypico2d import *
import room_select_state

SHADOW_SHOT = 0
# list = [slot, cooldown, name, strength, dexerity, magic, faith, power, critical_chance, accuracy]
#        [ 0        1       2      3         4        5      6      7           8            9    ]
skill_table = {
    SHADOW_SHOT: [0, 1, '그림자 사격', 0, 2, 0, 0, 0, 10, 90]
}

# list = [name, hp, barrior, shield, attack_damage, critical_chance, critical_damage, experience]
#        [ 0     1     2        3          4               5                 6             7    ]
# # self.hp, self.maxhp, self.barrior, self.shield, self.level = 100, 100, 0, 0, 1
#         self.name = '래빗'
#         self.attack_damage = 10
#         self.isAlive = True
#         self.monster_num = 0
#         self.experience = 0
(RABBIT, SAMURAI) = range(2)

monster_table = {
    RABBIT: ['래빗', 100, 0, 0, 10, 0, 0, 100],
    SAMURAI: ['사무라이', 80, 0, 0, 15, 15, 2, 100]
}

