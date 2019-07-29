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

    def beep(self):
        print('BEEP!')

    def __add__(self, other):
        result = self.get_seats() + other.get_seats()
        return result


class Bus(Automobile):
    _seats = 40
    _wheels = 6

    def beep(self):
        print('BEEP-BEEP!')


auto = Automobile()
print(auto.__class__)
print(auto.get_seats())
print(auto.get_electric())
print(auto.get_engine())
print(auto.get_wheels())
auto.beep()

bus = Bus()
print(bus.__class__)
print(bus.get_seats())
print(bus.get_electric())
print(bus.get_engine())
print(bus.get_wheels())
bus.beep()

print('-'*5)
print(bus + auto)