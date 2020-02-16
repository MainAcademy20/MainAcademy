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


def print_gameover(game_result):
    if game_result == 1:
        print('x победил!')
    if game_result == 2:
        print('o победил!')
    if game_result == 3:
        print('ничья!')
    input()


def clear_screen():
    if sys.platform in ['linux', 'darwin']:
        os.system('clear')
    if sys.platform == 'win32':
        os.system('cls')