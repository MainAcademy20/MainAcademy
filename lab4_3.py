word = 'Found name'
ids = {'name':'Oleg', 'age': 32}


def func(word, name, *args, age = 32):
    print(word,name)
    print("Age:",age)
    print (*args)

func(word,ids)
func(word, ids['name'],list(range(0,10)))
