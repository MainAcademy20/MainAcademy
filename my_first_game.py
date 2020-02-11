print("КРЕСТИКИ И НОЛИКИ")

print("Ознакомтесь с условиями игры:")

# Инструкция к Игре
print("При выборе хода вам необходимо указать номер позиции как указано на рисунке ниже")

game_map = list(range(1, 10))


def draw_board(game_map):
    print("-" * 13)
    for i in range(3):
        print("|", game_map[0 + i * 3], "|", game_map[1 + i * 3], "|", game_map[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(game_map[player_answer - 1]) not in "XO"):
                game_map[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_map):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game_map[each[0]] == game_map[each[1]] == game_map[each[2]]:
            return game_map[each[0]]
    return False


def main(game_map):
    counter = 0
    win = False
    while not win:
        draw_board(game_map)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(game_map)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(game_map)


main(game_map)

input("Нажмите Enter для выхода!")
