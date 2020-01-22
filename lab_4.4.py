'''
odd_foo = lambda x, y, z, w, q: [f for f in (x, y, z, w, q) if f % 2 == 1]
i=odd_foo(1,2,3,4,5)
print(i)
'''
odd_foo = list(filter((lambda f: f % 2 == 1), (range (1, 6))))
