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

    def __eq__(self, other):
        result = self.__class__ == other.__class__
        return result

    def __neg__(self):
        result = self.get_seats() * -1
        return result


class Bus(Automobile):
    _seats = 40
    _wheels = 6

    def beep(self):
        print('BEEP-BEEP!')


class ElectricCar(Automobile):
    _seats = 4
    _electric = True

    def move(self):
        print('Wroom!')


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

print('-'*5)
bus1 = Bus()
electric_car1 = ElectricCar()
print(bus1 == electric_car1)

print('-'*5)
electric_car2 = ElectricCar()
print(electric_car1.__class__)
print(electric_car2.__class__)
print(electric_car1 == electric_car2)

print('-'*5)
print(electric_car1.__neg__())
