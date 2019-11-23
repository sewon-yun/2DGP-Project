import game_framework
import mypico2d
import battle_state
import room_select_state

mypico2d.open_canvas(600, 800)
game_framework.run(battle_state)
mypico2d.close_canvas()



