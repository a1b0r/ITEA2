list = [1, 2, 3]

b = list.__iter__()

print(b.__next__())
print(b.__next__())
print(b.__next__())
# StopIteration
print(b.__next__())