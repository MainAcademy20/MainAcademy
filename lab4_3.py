word = 'Found name: '
ids = {'name': 'Sergii', 'age': 10}


def found_data(word_, *args, name, age=20):
    print(word_, name)
    print('Age:', age)
    print(args)


args = list(range(0, 10))

found_data(word, **ids)
found_data(word, *args, name=ids['name'])
