class First3Surprise(object):
    def __init__(self, l):
        self.l = l
        self.i = None

    def __iter__(self):
        self.i = iter(self.l)
        return self

    def __next__(self):
        return next(self.i), 'surprise'


f = First3Surprise([1, 2, 3, 4, 5])
for element in f:
    print(element)

 
