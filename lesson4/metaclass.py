
class MyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)


class TestingMeta(metaclass=MyMetaClass):

    _field = "Field"

    def __init__(self):
        self._var = 100
        self._new_var = 200
