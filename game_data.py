from mypico2d import *
import room_select_state

(SHADOW_SHOT, RANGED_SHOT, AIMING, BACKSTAB, BACKSTEP, CURE, FIRSTAID, HEALING, HIGH_HEALING, FULL_HEALING) = range(10)
# list = [ cooldown, name, strength, dexerity, magic, faith, power, critical_chance, kinds]
#        [     1       2      3         4        5      6      7           8           9  ]
skill_table = {
    SHADOW_SHOT: [2, '그림자 사격', 0, 2, 0, 0, 0, 0],
    RANGED_SHOT: [0, '사격', 0, 1, 0, 0, 0, 0],
    AIMING: [1, '정조준', 0, 1, 0, 0, 0, 0],
    BACKSTAB: [4, '암습', 0, 3.6, 0, 0, 0, 0],
    BACKSTEP: [1, '백스텝', 0, 0, 0, 0, 0.65, 1],
    CURE: [0, '상처 치료', 0, 0, 0, 0, 0.3, 3],
    FIRSTAID: [0, '응급 처치', 0, 0, 0, 0, 0.1, 3],
    HEALING: [2, '회복', 0, 0, 0, 0, 0.25, 3],
    HIGH_HEALING: [4, '상급 회복', 0, 0, 0, 0, 0.5, 3],
    FULL_HEALING: [8, '완전 회복', 0, 0, 0, 0, 1, 3]
}

# list = [name, hp, barrior, shield, attack_damage, critical_chance, critical_damage, experience]
#        [ 0     1     2        3          4               5                 6             7    ]
# # self.hp, self.maxhp, self.barrior, self.shield, self.level = 100, 100, 0, 0, 1
#         self.name = '래빗'
#         self.attack_damage = 10
#         self.isAlive = True
#         self.monster_num = 0
#         self.experience = 0
(RABBIT, SAMURAI, PROPHET, ROCK, TRENT, DURAHAN, CYCLOPS, BUDYFUCKER, ANCIENT) = range(9)

monster_table = {
    RABBIT: ['래빗', 100, 0, 0, 10, 0, 0, 100],
    SAMURAI: ['사무라이', 120, 0, 0, 25, 15, 2, 100],
    PROPHET: ['예언가', 80, 0, 0, 30, 0, 0, 100],
    ROCK: ['바위', 200, 0, 0, 25, 0, 0, 100],
    TRENT: ['트렌트', 150, 0, 0, 15, 0, 0, 100],
    DURAHAN: ['듀라한', 150, 0, 0, 30, 0, 0, 100],
    CYCLOPS: ['외눈박이', 200, 0, 0, 25, 0, 0, 100],
    BUDYFUCKER: ['고문관', 180, 0, 0, 30, 0, 0, 100],
    ANCIENT: ['고대의 것', 1, 250, 0, 0, 20, 0, 0, 100]
}

(PHOENIX) = 0

boss_monster_table = {
    PHOENIX: ['불사조', 500, 0, 0, 40, 10, 5, 300]
}

a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = range(1, 16)

experence_table = {
    a1: 100, a2: 200, a3: 300, a4: 400, a5: 500, a6: 600, a7: 700, a8: 800, a9: 900, a10: 1000, a11: 1100,
    a12: 1200, a13: 1300, a14: 1400, a15: 1500
}
