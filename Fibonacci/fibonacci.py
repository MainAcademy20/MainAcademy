class Fibo:
    def __init__(self, n):
        self.n = int(n)
        self.fib1 = self.next = 0
        self.fib2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.next = self.fib1 + self.fib2
        if self.next < self.n:
            self.fib2, self.fib1 = self.next, self.fib2
        else:
            raise StopIteration
        return self.fib2


n = input("Input Fibonacci max: ")
f = Fibo(n)
for el in f:
    print(el)