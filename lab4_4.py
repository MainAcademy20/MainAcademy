foo = [1, 2, 3, 4, 5]

odd_foo1 = list(filter(lambda x: x%2 == 1,foo))
print(odd_foo1)
odd_foo2 = [x for x in foo if x%2 ==1]
print(odd_foo2)
