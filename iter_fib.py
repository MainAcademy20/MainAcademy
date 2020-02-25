class Fibo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


n = int(input('Input Fibonacci max: '))
f = Fibo(n)
for number in f:
    print(number)
