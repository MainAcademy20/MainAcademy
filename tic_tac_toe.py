import os

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
chars = ['X', 'O']


def get_pretty_format(*args):
    """
    {0}{1}{2}
    {3}{4}{5}
    {6}{7}{8}
    """
    print('\n{} | {} | {} \n——————————\n'
          '{} | {} | {} \n——————————\n'
          '{} | {} | {}'.format(*args))


def take_index():
    """
    Function returns index from 0 to 9 (type int)
    """
    number = None
    while number not in range(9):
        try:
            number = int(input('\nChoose a number where to put: '))
        except ValueError:
            print('Wrong number!')
    return number


def make_changes(local_arr, index, local_char):
    """
    Function overrides existing array and returns it
    """
    while local_arr[index] == 'X' or local_arr[index] == 'O':
        print('This place is taken!')
        index = take_index()
    local_arr[index] = local_char
    return local_arr


def check_win(local_arr):
    for i in [0, 3, 6]:
        if local_arr[i] == local_arr[i + 1] == local_arr[i + 2]:
            return True
    for i in [0, 1, 2]:
        if local_arr[i] == local_arr[i + 3] == local_arr[i + 6]:
            return True
    if local_arr[0] == local_arr[4] == local_arr[8]:
        return True
    elif local_arr[2] == local_arr[4] == local_arr[6]:
        return True
    else:
        return False


def check_draw(local_arr):
    return all(map(lambda x: type(x) == str, local_arr))


def reload_game():
    global arr
    choose = input('Do you want to play again? choose "y" or "n": ')
    if choose == 'y':
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    else:
        exit()


while True:
    for char in chars:
        get_pretty_format(*arr)
        print('\nPlayer %s moves' % char)
        global_index = take_index()
        arr = make_changes(arr, global_index, char)
        if check_win(arr):
            os.system('clear')
            get_pretty_format(*arr)
            print('\nPlayer %s won! Congratulations!!\n' % char)
            reload_game()
        if check_draw(arr) and not check_win(arr):
            os.system('clear')
            get_pretty_format(*arr)
            print('\nDraw!')
            reload_game()
        os.system('clear')
