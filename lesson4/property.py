class Test:

    def __init__(self, x):
        print('init called')
        self._x = x

    def get_x(self):
        print('get called')
        return self._x

    def set_x(self, x):
        print('set called')
        if x > 10:
            raise ValueError('x must be less then 10')
        self._x = x

    def del_x(self):
        print('del called')
        del self._x

    x = property(fget=get_x, fset=set_x, fdel=del_x)


obj = Test(100)
obj.x
obj.x = 9
del obj.x