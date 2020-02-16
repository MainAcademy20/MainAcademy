import view
from model import XOState


def get_new_game_status(xostate):
    """TODO::убрать дублирующийся код"""
    for i in range(3):
        row = xostate.get_row(i)
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    for i in range(3):
        col = xostate.get_col(i)
        if col[0] == col[1] == col[2] and col[0] != 0:
            return col[0]
    for i in range(2):
        diag = xostate.get_diag(i)
        if diag[0] == diag[1] == diag[2] and diag[0] != 0:
            return diag[0]
    for i in range(3):
        row = xostate.get_row(i)
        for cell in row:
            if cell == 0:
                return 0
    return 3


def check_input(local_turn, state, keys):
    view.clear_screen()
    view.print_field(state)
    if local_turn not in ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']:
        view.show_error('1')
        return False
    if state.field[keys[local_turn][0]][keys[local_turn][1]] in [1, 2]:
        view.show_error('2')
        return False
    return True


def game_loop():
    """
         TODO::* добавить проверки на корректность ввода
         TODO::* если ввод некорректен, повторить его не меняя игрока
         TODO::** спросить, хотят ли игроки сыграть еще раз (правильно структурировать код)
         TODO::*** переписать так чтобы можно было играть с компьютером + выбирать режим

    """
    key_to_pos = {
        'q': (0, 0), 'w': (0, 1), 'e': (0, 2),
        'a': (1, 0), 's': (1, 1), 'd': (1, 2),
        'z': (2, 0), 'x': (2, 1), 'c': (2, 2),
    }

    state = XOState()
    game_status = 0
    while game_status == 0:
        view.clear_screen()
        view.print_field(state)
        turn = view.get_input(state)
        while not check_input(turn, state, key_to_pos):
            turn = view.get_input(state)
        pos_row, pos_col = key_to_pos[turn]
        state.set_cell(pos_row, pos_col, state.current_player)
        state.switch_player()
        game_status = get_new_game_status(state)
    view.clear_screen()
    view.print_field(state)
    view.print_gameover(game_status)


if __name__ == '__main__':
    game_loop()