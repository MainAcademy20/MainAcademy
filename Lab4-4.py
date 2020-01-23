foo = [1, 2, 3, 4, 5]

# odd_foo = []
#
#
# def isOdd(x):
#     return x % 2 == 1
#
#
# for f in foo:
#     if isOdd(f):
#         odd_foo.append(f)
#     print(odd_foo)

print([num for num in foo if num % 2 == 1])
print(list(filter(lambda x: x % 2 == 1, foo))) #OLEG
