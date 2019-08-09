list = [1, 2, 3]


class Test():

    def __init__(self):
        self._a = 1
        self._b = 2


our_list = iter(list)

print(Test().__dict__())
a = Test()
print(a.__dict__())
print(vars(a))

