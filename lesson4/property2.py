class Test:

    def __init__(self, x):
        print('init called')
        self._x = x

    @property
    def x(self):
        print('get called')
        return self._x

    @x.setter
    def x(self, x):
        print('set called')
        if x > 10:
            raise ValueError('x must be less then 10')
        self._x = x

    @x.deleter
    def x(self):
        print('del called')
        del self._x


obj = Test(100)
obj.x
obj.x = 9
del obj.x