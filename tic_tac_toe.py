board = [['_' for j in range(3)] for i in range(3)]
player = 'X'

def PrintBoard():
    print('поле имеет систему координат [x y] где x - №строки y - №колонки')
    for i in range(3):
        row = '| '
        for j in range(3):
            row += (board[i][j] + ' | ')
        print(row)

def MoveCheck(player):
    move = False
    row, col = AskMove()
    while not move:
        if row >= 3 or row < 0 or col >= 3 or col < 0:
            print ('Некорректный ход , номер строки и/или колонки должен быть от 1 до 3')
            row, col = AskMove()
        elif board[row][col] != '_':
            print('Эта клетка занята , выберите другую')
            row, col = AskMove()
        else:
            board[row][col] = player
            move = True

def SwitchPlayer(player):
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    return player

def AskMove():
    row = int(input('Введите номер строки: ')) - 1
    col = int(input('Введите номер колонки: ')) - 1
    return row, col

def PlayerMove(player):
    print('Сейчас ходит %s ' % player)

def Game(player):
    PrintBoard()
    move_counts = 1
    while move_counts <= 10:
        PlayerMove(player)
        MoveCheck(player)
        PrintBoard()
        if CheckWin():
            print('Победил %s ' % player)
            break
        else:
            player = SwitchPlayer(player)
            move_counts += 1
        if move_counts == 10 :
            print('Ничья')
            break

def CheckWin():
    for rowcol in range(3):
        if board[rowcol][0] == board[rowcol][1] == board[rowcol][2] != '_' or board[0][rowcol] == board[1][rowcol] == board[2][rowcol] != '_':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '_' or board[0][2] == board[1][1] == board[2][0]  != '_':
        return True
    return False

def ResetBoard():
   global board
   board = [['_' for j in range(3)] for i in range(3)]

while True:
    Game(player)
    replay = input('Хотите сыграть еще раз? (y/n): ')
    if replay == 'n' or replay == 'N':
        break
    elif replay == 'y' or replay == 'Y':
        ResetBoard()
        continue
    elif replay != 'y' or 'Y' or 'n' or 'N':
        break