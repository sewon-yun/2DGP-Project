from mypico2d import *
import room_select_state

(SHADOW_SHOT, RANGED_SHOT, AIMING, BACKSTAB, BACKSTEP, CURE, FIRSTAID, HEALING, HIGH_HEALING, FULL_HEALING) = range(10)
# list = [ cooldown, name, strength, dexerity, magic, faith, power,  kinds, sound]
#        [     1       2      3         4        5      6      7       8      9  ]
# SOUND = KNIFE, GUN, BOW
skill_table = {
    SHADOW_SHOT: [2, '그림자 사격', 0, 2, 0, 0, 0, 0, 2],
    RANGED_SHOT: [0, '사격', 0, 1, 0, 0, 0, 0, 2],
    AIMING: [1, '정조준', 0, 1, 0, 0, 0, 0, 1],
    BACKSTAB: [4, '암습', 0, 3.6, 0, 0, 0, 0, 0, 0],
    BACKSTEP: [1, '백스텝', 0, 0, 0, 0, 0.65, 1, 0],
    CURE: [0, '상처 치료', 0, 0, 0, 0, 0.1, 3, 0],
    FIRSTAID: [0, '응급 처치', 0, 0, 0, 0, 0.1, 3, 0],
    HEALING: [2, '회복', 0, 0, 0, 0, 0.25, 3, 0],
    HIGH_HEALING: [4, '상급 회복', 0, 0, 0, 0, 0.5, 3, 0],
    FULL_HEALING: [8, '완전 회복', 0, 0, 0, 0, 1, 3, 0]
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
    RABBIT: ['래빗', 100, 0, 0, 20, 0, 0, 100],
    SAMURAI: ['사무라이', 120, 0, 0, 25, 15, 2, 100],
    PROPHET: ['예언가', 100, 0, 0, 60, 0, 0, 100],
    ROCK: ['바위', 200, 0, 0, 40, 0, 0, 100],
    TRENT: ['트렌트', 300, 0, 0, 25, 0, 0, 100],
    DURAHAN: ['듀라한', 150, 0, 0, 30, 0, 0, 100],
    CYCLOPS: ['외눈박이', 200, 0, 0, 25, 0, 0, 100],
    BUDYFUCKER: ['고문관', 180, 0, 0, 30, 0, 0, 100],
    ANCIENT: ['고대의 것', 1, 300, 0, 30, 0, 0, 100]
}

(PHOENIX, VAMPIRE, DEATH, LILITH, CONCUBINE, KING) = range(6)

boss_monster_table = {
    PHOENIX: ['불사조', 500, 0, 0, 40, 10, 5, 300],
    VAMPIRE: ['뱀파이어 로드', 250, 250, 0, 30, 20, 5, 300],
    DEATH: ['데스', 1, 500, 0, 50, 10, 5, 300],
    LILITH: ['릴리스', 100, 600, 0, 40, 10, 5, 500],
    CONCUBINE: ['패왕의 첩', 700, 0, 0, 40, 10, 5, 700],
    KING: ['고대의 패왕', 1000, 500, 0, 60, 10, 5, 1000]
}

(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15,
 a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30) = range(1, 31)

experence_table = {
    a1: 100, a2: 300, a3: 500, a4: 700, a5: 900, a6: 1200, a7: 1500, a8: 1800, a9: 2100, a10: 2400, a11: 2800,
    a12: 3200, a13: 3600, a14: 4000, a15: 4400, a16: 4900, a17: 5400, a18: 5900, a19: 6400, a20: 7000, a21: 7700,
    a22: 8400, a23: 10000, a24: 11000, a25: 12100, a26: 13200, a27: 14400, a28: 15600, a29: 17800, a30: 20000
}
