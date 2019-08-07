class Automobile:
    _seats = 4  # public
    _wheels = 4  # protected
    _engine = 'V8'
    _electric = False

    def set_seats(self, seats):
        self._seats = seats

    def get_seats(self):
        return self._seats

    def get_wheels(self):
        return self._wheels

    def get_engine(self):
        return self._engine

    def get_electric(self):
        return self._electric


car = Automobile()
car.set_seats(8)
print(car.get_seats())

print(Automobile._seats)
