class Fibonacci:
    def __init__(self, count_numbers):
        self.count_numbers = count_numbers
        self.first_number = 1
        self.second_number = 1
        self.support_variable = None  # this variable needs to saves temporary value of 'second_number'
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.step += 1
        if self.step <= 2:
            return 1
        self.support_variable = self.second_number
        self.second_number = self.second_number+self.first_number
        self.first_number = self.support_variable
        if self.step >= self.count_numbers+1:
            raise StopIteration
        return self.second_number


if __name__ == "__main__":
    n = int(input())
    f = Fibonacci(n)
    for number in f:
        print(number)