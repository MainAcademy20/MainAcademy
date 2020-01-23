word = "Found name: "
ids = {"name": "Marina", "age": 20}

def get_name_age(local_word, *args, name, age=()):
    print(local_word, name)
    print("Age:", age)
    print(args)


get_name_age(word, **ids)
get_name_age()
