seq1 = list(range(10))
seq2 = list(range(0, 10, 2))
res = []


def intersection(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


print(intersection(seq1, seq2))
print('list', res)
