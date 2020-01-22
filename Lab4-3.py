word = 'Found name:'
ids = {'name': 'Vasya', 'age': 19}


def personal_data_finder(local_word, *args, name, age=None):
    print(local_word, name)
    print("Age:", age)
    print(args)


personal_data_finder(word, **ids)
personal_data_finder(word, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, name=ids['name'])
