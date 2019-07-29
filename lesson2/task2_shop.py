class Shop:

    _name = None
    _sales = 0

    def __init__(self, name, sales=0):
        self._name = name
        self._sales = sales