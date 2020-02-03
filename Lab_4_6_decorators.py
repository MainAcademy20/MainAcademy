def bread(func):
    def wrapper():
        print()
        func()
        print("<\_________/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper
