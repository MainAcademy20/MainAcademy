import view
from model import XOState
import random


def get_new_game_status(xostate):
    """Done TODO::убрать дублирующийся код"""
    row = find_winner(xostate.get_row, 3)
    col = find_winner(xostate.get_col, 3)
    diag = find_winner(xostate.get_diag, 2)
    for winner in (row, col, diag):
        if winner is not None:
            return winner
    for i in range(3):
        row = xostate.get_row(i)
        for cell in row:
            if cell == 0:
                return 0
    return 3


def find_winner(func, number):
    for i in range(number):
        item_name = func(i)
        if item_name[0] == item_name[1] == item_name[2] and item_name[0] != 0:
            return item_name[0]


def make_bot_turn(state, keys):
    pool = [letter for letter in keys.keys() if state.field[keys[letter][0]][keys[letter][1]] not in [1, 2]]
    bot_turn = random.randint(0, len(pool)-1)
    return pool[bot_turn]


def get_turn(state, mode, keys):
    if mode == '1':
        turn = view.get_input(state)
        while not check_input(turn, state, keys):
            turn = view.get_input(state)
        return turn
    if mode == '2':
        if state.current_player == 1:
            turn = view.get_input(state)
            while not check_input(turn, state, keys):
                turn = view.get_input(state)
            return turn
        if state.current_player == 2:
            turn = make_bot_turn(state, keys)
            return turn


def check_input(local_turn, state, keys):
    view.clear_screen()
    view.print_field(state)
    if local_turn not in keys.keys():
        view.show_error('1')
        return False
    if state.field[keys[local_turn][0]][keys[local_turn][1]] in [1, 2]:
        view.show_error('2')
        return False
    return True


def game_loop():
    """
         Done TODO::* добавить проверки на корректность ввода
         Done TODO::* если ввод некорректен, повторить его не меняя игрока
         Done TODO::** спросить, хотят ли игроки сыграть еще раз (правильно структурировать код)
         Done TODO::*** переписать так чтобы можно было играть с компьютером + выбирать режим

    """
    key_to_pos = {
        'q': (0, 0), 'w': (0, 1), 'e': (0, 2),
        'a': (1, 0), 's': (1, 1), 'd': (1, 2),
        'z': (2, 0), 'x': (2, 1), 'c': (2, 2),
    }

    state = XOState()
    game_status = 0
    mode = view.show_game_menu()
    while game_status == 0:
        view.clear_screen()
        view.print_field(state)
        turn = get_turn(state, mode, key_to_pos)
        pos_row, pos_col = key_to_pos[turn]
        state.set_cell(pos_row, pos_col, state.current_player)
        state.switch_player()
        game_status = get_new_game_status(state)
    view.clear_screen()
    view.print_field(state)
    view.print_game_over(game_status)
    if view.play_again(input('\nDo you want to play again? Type \'y\': ')):
        game_loop()


if __name__ == '__main__':
    game_loop()