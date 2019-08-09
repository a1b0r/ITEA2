list = [1, 2, 3]

class Test():
    __slots__ = '_a', '_b'

    def __init__(self):
        self._a = 1
        self._b = 2

our_list = iter(list)

a = Test()
print(a.__slots__)
print(a._a, a._b)

