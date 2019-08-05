
class MyMetaClass(type):

    def __new__(cls, name, bases, attributes):
        if "attr" not in attributes:
            attributes["attr"] = True

        return super().__new__(cls, name, bases, attributes)


class TestingMeta(metaclass=MyMetaClass):

    _field = "Field"

    def __init__(self):
        self._var = 100
        self._new_var = 200


TestingMeta.a = True
print(TestingMeta.__dict__)