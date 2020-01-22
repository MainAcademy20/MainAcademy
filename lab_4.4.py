'''
foo = [1, 2, 3, 4, 5]
odd_foo = [f for f in foo if f % 2 == 1]
'''

odd_foo = lambda x, y, z, w, q: [f for f in (x, y, z, w, q) if f % 2 == 1]
'''
i=odd_foo(1,2,3,4,5)
print(i)
'''