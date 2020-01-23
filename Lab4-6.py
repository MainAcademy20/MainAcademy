
def decorator(func):
    def wrapper(*args):
        print(*args)
        print(func(*args))
        print('Bye')
    return wrapper


@decorator
def generate_recipe(*args):
    recipe_local, counter = '', 0
    exit_arr = []
    for arg in args:
        counter += 1
        exit_arr.append('{}. {}'.format(counter, arg))
    return '\n'.join(exit_arr)


generate_recipe('Лук', 'Чеснок', 'Хлеб')
# generate_recipe_dec = decorator(generate_recipe)
# generate_recipe_dec('Лук', 'Чеснок', 'Хлеб')
