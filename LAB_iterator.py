"""
Реализовать такой итератор
class Fibo:
   def _init__(self, n): ...
   def _iter_: ...
   def _next_: ...
чтобы потом я мог сделать:

n = input("Input Fibonacci max: ")
f = Fibo(n)
for number in f:
   print(number)

и увидеть все числа Фибоначчи
1
1
2
3
...
и когда следующее будет больше N - цикл должен кончиться
"""
class Fibo(object):
    def __init__(self, n):
        self.n = n
        self.list_n = list(range(self.n))
        print(self.list_n)
        self.i = None

    def __iter__(self):
        self.i = iter(self.list_n[:])
        return self.i

    def __next__(self):
        self.fib1 = next(self.i)
        self.fib2 = next(self.i)
        print("111", self.fib1)
        print("222", self.fib2)
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        self.sum_f = self.fib1 + self.fib2
        return self.sum_f

"""
    def __next__(self):
        a, b = b, a + b
        a = b = next(self.i)
        return b

"""


a = 20
f = Fibo(a)
for number in f:
    print("---", number)

