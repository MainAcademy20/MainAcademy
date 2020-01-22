var1 = list(range(0,10))
var2 = list(range(0,10,2))


def intersection(arg1, arg2):
    res = []
    for i in arg2:
        for j in arg1:
            if i == j:
                res.append(i)
    return res


rez = intersection(var1, var2)
print(rez)
