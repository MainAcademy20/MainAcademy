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
            os.system('clear')
        except ValueError:
            print('Wrong number!')
    return number


def make_changes(local_arr, index, local_char):
    """
    Function overrides existing array and returns it
    """
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


get_pretty_format(*arr)
while True:
    for char in chars:
        print('\nPlayer %s moves' % char)
        global_index = take_index()
        os.system('clear')
        arr = make_changes(arr, global_index, char)
        get_pretty_format(*arr)
        if check_win(arr):
            print('\nYou won! Congratulations!!')
            exit()
