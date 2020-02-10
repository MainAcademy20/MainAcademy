n = 3
m = 3
counter = 0
pole_game = [[" "] * m for i in range(n)]


def pole_game_print():
    for element in pole_game:
        print("--------------")
        print("|", element[0], "|", element[1], "|", element[2], "|")
    print("--------------")


pole_game_print()


def cell():
    print("Player make your choice with", choice)
    while True:
        try:
            r = int(input("input row (1-3):"))
            break
        except ValueError:
            print("incorrect inputs")
    while True:
        try:
            c = int(input("input column (1-3):"))
            break
        except ValueError:
            print("incorrect inputs")
    return r, c


def input_cell(a, b, n):
    if 1 <= a <= 3 and 1 <= b <= 3:
        if pole_game[a - 1][b - 1] == " ":
            pole_game[a - 1][b - 1] = choice
            n += 1
        else:
            print("cell is not empty")
        return pole_game[a - 1][b - 1], n
    print("incorrect index")


def win_check(pol_game):
    w = False
    for i in range(3):
        if pole_game[i][0] == pole_game[i][1] == pole_game[i][2] != " ":
            w = True
    for j in range(3):
        if pole_game[0][j] == pole_game[1][j] == pole_game[2][j] != " ":
            w = True
    if pole_game[0][0] == pole_game[1][1] == pole_game[2][2] != " ":
        w = True
    if pole_game[0][2] == pole_game[1][1] == pole_game[2][0] != " ":
        w = True
    return w


while counter < 9:
    if counter % 2 == 0:
        choice = 'O'
    else:
        choice = 'X'
    r, c = cell()
    pole_game[r - 1][c - 1], counter = input_cell(r, c, counter)
    pole_game_print()
    win = win_check(pole_game)
    if win:
        print("Player with", choice, ", Your are the winner!!!")
        break

print("game is over")
