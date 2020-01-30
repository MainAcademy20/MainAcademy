arg1 = list(range(0, 10))
arg2 = list(range(0, 10, 2))

def func(arg1, arg2):
    res = []
    for x in arg1:
        if x in arg2:
            res.append(x)
    return res

print(func(arg1, arg2))