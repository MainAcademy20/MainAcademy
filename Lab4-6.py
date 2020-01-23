
def decorator(func):
    def wrapper(*args):
        print(*args)
        func(*args)
        print(func(*args))
    return wrapper


@decorator
def generate_recipe(*args):
    recipe_local, counter = '', 0
    exit_arr = []
    print('We\'re inside the function')
    for arg in args:
        counter += 1
        exit_arr.append('{}. {}'.format(counter, arg))
    return '\n'.join(exit_arr)


generate_recipe('Лук', 'Чеснок', 'Хлеб')
# generate_recipe_dec = decorator(generate_recipe)
# generate_recipe_dec('Лук', 'Чеснок', 'Хлеб')
