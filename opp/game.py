import view
from model import XOState
import time


def get_new_game_status(xostate, f, n):
    """TODO::убрать дублирующийся код + """
    for i in range(n):
        p = f(i)
        if p[0] == p[1] ==p[2] and p[0] != 0:
            return p[0]
        for i in range(3):
            row = xostate.get_row(i)
        for cell in row:
            if cell == 0:
                return 0
    return 3


def game_loop():
    """
         TODO::* добавить проверки на корректность ввода +
         TODO::* если ввод некорректен, повторить его не меняя игрока +
         TODO::** спросить, хотят ли игроки сыграть еще раз (правильно структурировать код) +
         TODO::*** переписать так чтобы можно было играть с компьютером + выбирать режим

    """
    key_to_pos = {
        'q': (0, 0), 'w': (0, 1), 'e': (0, 2),
        'a': (1, 0), 's': (1, 1), 'd': (1, 2),
        'z': (2, 0), 'x': (2, 1), 'c': (2, 2),
    }
    spisok = ['q','w','e','a','s','d','z','x','c']

    state = XOState()
    game_status = 0
    if view.start_game():
        com_game_status = 1
    else:
        com_game_status = 0
    while game_status == 0:
        view.print_field(state)
        if com_game_status == 0:
            turn = view.get_input(state)
        else:
            turn = view.get_comp_input(state,spisok)
        if view.is_space_free(spisok, turn):
            pos_row, pos_col = key_to_pos[turn]
            if state.get_yacheika(pos_row, pos_col) == 0:
                state.set_cell(pos_row, pos_col, state.current_player)
            else:
                print('the cell is already filled')
                input()
                state.switch_player()
        else:
            print('incorrect input')
            input()
            state.switch_player()
        state.switch_player()
        view.clear_screen()
        game_status = get_new_game_status(state, state.get_row, 3)
        game_status = get_new_game_status(state, state.get_col,3)
        game_status = get_new_game_status(state, state.get_diag, 2)
        if game_status > 0:
            view.clear_screen()
            view.print_field(state)
            view.print_gameover(game_status)
            if view.new_game():
                game_status = 0
                print(com_game_status)
                for i in range(3):
                    for j in range(3):
                        state.set_yacheika(i,j)
                        state.current_player = 1


if __name__ == '__main__':
    game_loop()
