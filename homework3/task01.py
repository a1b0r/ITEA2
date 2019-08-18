class Dot:

    _x = 0
    _y = 0
    _z = 0

    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    def __mul__(self, other):
        return Dot(self.get_x() * other.get_x(), self.get_y() * other.get_y(), self.get_z() * other.get_z())

    def __add__(self, other):
        return self.get_x() + other.get_x(), self.get_y() + other.get_y(), self.get_z() + other.get_z()

    def __sub__(self, other):
        return self.get_x() - other.get_x(), self.get_y() - other.get_y(), self.get_z() - other.get_z()

    def __neg__(self):
        result = self.get_x() * -1, self.get_y() * -1, self.get_z() * -1
        return result

    def __str__(self):
        return '({}, {}, {})'.format(self._x, self._y, self._z)


dot1 = Dot(1, 2, 3)
dot2 = Dot(1, 2, 3)
print(dot1)
print(dot2)
print('-'*5)

print(dot1 + dot2)
print(dot1 - dot2)
print('-'*5)

print(-dot1)
print('-'*5)

dot3 = dot1 * dot2
print(dot3)