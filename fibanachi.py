class Fibo:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.f1 = 1
        self.f2 = 1

    def __next__(self):
        if self.f1 < self.limit:
            a = self.f1
            self.f1, self.f2 = self.f2, self.f1 + self.f2
            return a
        else:
            raise StopIteration


n = int(input("Input Fibonacci max: "))
f = Fibo(n)
for number in f:
    print(number)
