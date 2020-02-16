"""
вывести на экран:
    игровое поле
    состояние игры
    запросить ввод текущего игрока
    если надо, сообщение об ошибке

o . .
. . x
. . .

x|o > q|w|e|a|s|d|z|x|c
x|o победил!
ничья!
"""
import os
import sys


def show_game_menu():
    print('\nWelcome to the game!!!\n')
    print('Press 1 to play single game or 2 to play against PC\n')
    mode = input('What mode would you like to play?: ')
    return mode


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
        print()


def get_input(xostate):
    if xostate.current_player == 1:
        print('\nx > ', end='')
    if xostate.current_player == 2:
        print('\no > ', end='')
    return input()


def show_error(error):
    if error == '1':
        print('Wrong input!\nUse the following keys:\n\nq w e\na s d\nz x c')
    if error == '2':
        print('\nThis place is taken!\nTry again:')


def print_game_over(game_result):
    if game_result == 1:
        print('\nx победил!')
    if game_result == 2:
        print('\no победил!')
    if game_result == 3:
        print('\nничья!')


def play_again(choose):
    if choose == "y":
        print('Lets play again!')
        return True
    else:
        print('\n================Bye!================\n')
        return False


def clear_screen():
    if sys.platform in ['linux', 'darwin']:
        os.system('clear')
    if sys.platform == 'win32':
        os.system('cls')