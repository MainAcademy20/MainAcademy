b = [i for i in range(1,6)]


def numerate (spisok):
   for i in spisok:
        yield spisok.index(i),i



print(list(numerate(b)))




