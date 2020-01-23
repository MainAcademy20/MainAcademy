ids = {'name': 'Alisa', 'age': '27'}
word = 'Found name'


def found_name(words, *args, name, age=None):
    print(word, name)
    print('Age:', age)
    print(args)


args = list(range(0, 10))

found_name(word, **ids)
found_name(word, *args, name=ids['name'])
