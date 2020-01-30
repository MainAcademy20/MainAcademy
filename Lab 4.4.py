foo = [1, 2, 3, 4, 5]
odd_foo = []

isOdd = lambda f: f % 2 == 1
for f in foo:
    if isOdd(f):
        odd_foo.append(f)

print(odd_foo)
