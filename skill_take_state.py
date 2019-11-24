import game_framework
from mypico2d import *
import battle_state
import room_select_state
import random
from character import Skill

from background import Background
from cursor import Cursor


name = "SkillTakeState"
background = None
image = None
cursor = None
dialog = None
skill = None
arrow = None
dialog_yes_or_no = None
font_size_20 = None
font_size_25 = None
font_size_30 = None
max_select_times, select_times = 5, 5
num = 0
count = 0
x, y = 0, 0


def enter():
    global background, cursor, dialog, dialog_yes_or_no, font_size_30, font_size_25, font_size_20, \
        x, y, num, count, select_times, skill, arrow
    background = Background()
    cursor = Cursor()
    skill = Skill()
    skill.skill_pick = True
    pick = random.randint(0, 9)
    if pick == 4:
        pick += 1
    skill.create(pick)
    cursor.x, cursor.y = x, y
    select_times = 5
    num = 0
    count = battle_state.count
    if image == None:
        dialog = load_image('dialog200x60.png')
        dialog_yes_or_no = load_image('dialog200x70.png')
        font_size_30 = load_font('gothic.ttf', 30)
        font_size_25 = load_font('gothic.ttf', 25)
        font_size_20 = load_font('gothic.ttf', 20)
        arrow = load_image('arrow.png')
    if count == 0:
        game_framework.push_state(room_select_state)
    else:
        battle_state.character.skills[0].skill_select = True

def exit():
    global background, cursor, dialog, dialog_yes_or_no, font_size_30, font_size_25, font_size_20, skill
    del background, cursor, dialog, dialog_yes_or_no, font_size_30, font_size_25, font_size_20, skill


def handle_events():
    global cursor, select_times, x, y, num, skill, count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(room_select_state)
                room_select_state.x, room_select_state.y = cursor.x, cursor.y
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y
                cursor.x, cursor.y = x, y
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if 325 <= cursor.x <= 575 and 463 <= cursor.y <= 537:
                    if select_times > 0:
                        select_times -= 1
                        # 스킬 다시 뽑기
                        pick = random.randint(0, 9)
                        if pick == 4:
                            pick += 1
                        skill.create(pick)
                elif 25 <= cursor.x <= 275 and 463 <= cursor.y <= 537:
                    battle_state.character.skills[num].skill_select = False
                    num += 1
                    if num == 5:
                        num = 0
                    battle_state.character.skills[num].skill_select = True

                elif 5 <= cursor.x <= 275 and 53 <= cursor.y <= 147:
                    room_select_state.x, room_select_state.y = x, y
                    battle_state.character.skills[num].skill_select = False
                    game_framework.push_state(room_select_state)

                elif 325 <= cursor.x <= 595 and 53 <= cursor.y <= 147:
                    room_select_state.x, room_select_state.y = x, y
                    # 스킬 내용 수락
                    battle_state.character.skills[num].skill_select = False
                    skill.skill_pick = False
                    skill.slot = num
                    battle_state.character.skills[num] = skill
                    game_framework.push_state(room_select_state)
def draw():
    global skill
    clear_canvas()
    background.draw()
    dialog.clip_draw(0, 0, 200, 60, 150, 500, 250, 75)
    dialog.clip_draw(0, 0, 200, 60, 450, 500, 250, 75)
    dialog_yes_or_no.clip_draw(0, 0, 200, 70, 140, 100, 270, 95)
    dialog_yes_or_no.clip_draw(0, 0, 200, 70, 460, 100, 270, 95)
    font_size_25.draw(90, 500, '슬롯 바꾸기', (255, 255, 255))
    font_size_25.draw(400, 510, '다시 뽑기', (255, 255, 255))
    font_size_20.draw(410, 490, '%3.0f  /%3.0f' % (select_times, max_select_times), (255, 255, 255))
    font_size_30.draw(115, 100, '무시', (255, 255, 255))
    font_size_30.draw(435, 100, '수락', (255, 255, 255))
    arrow.clip_draw(0, 0, 100, 70, 300, 350, 100, 70)
    if battle_state.character.skills[num].name == skill.name:
        font_size_20.draw(240, 300, 'Skill Level Up +', (255, 255, 0))
    battle_state.character.skills[num].draw()
    skill.draw()
    cursor.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
