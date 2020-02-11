def print_field(xostate):
    for i in range(3):
        row = xostate.get_row(i)
        for cell in row:
            if cell == 0:
                print('.', end=' ')
            if cell == 1:
                print('x', end=' ')
            if cell == 2:
                print('o', end=' ')


def get_input(xostate):
    if xostate.current_player == 1:
        print('x >', end=' ')
    if xostate.current_player == 2:
        print('o >', end=' ')
    return input()


def print_gameover(game_result):
    if game_result == 1:
        print('x is winner')
    if game_result == 2:
        print('o is winner')
    if game_result == 3:
        print('draw')
    input()