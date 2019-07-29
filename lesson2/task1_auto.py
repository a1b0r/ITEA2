class Automobile:
    _wheels = 4
    _doors = 2
    _name = None
    _color = None

    def get_name(self):
        return self._name

    def get_wheels(self):
        return self._wheels

    def get_doors(self):
        return self._doors

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def beep(self):
        print('Beep!')


class CargoAutomobile(Automobile):
    _wheels = 6

    def __init__(self, name, color):
        self._name = name
        self._color = color


class PassAutomobile(Automobile):
    _doors = 4
    _electric = False

    def __init__(self, name, color, electric=False):
        self._name = name
        self._color = color
        self._electric = electric

    def set_doors(self,doors):
        self._doors = doors

    def print_electric(self):
        if self._electric:
            print("Electric")
        else:
            print("not Electric")

    def beep(self):
        print('Be-Beep!')


cargo_auto = CargoAutomobile('Volvo','blue')
print(cargo_auto.__class__)
print(cargo_auto.get_name())
print(cargo_auto.get_wheels())
print(cargo_auto.get_doors())

cargo_auto.beep()

pass_auto1 = PassAutomobile('Audi','white', True)
print(pass_auto1.__class__)
print(pass_auto1.get_name())
print(pass_auto1.get_wheels())
print(pass_auto1.get_doors())
pass_auto1.print_electric()
pass_auto1.beep()

pass_auto2 = PassAutomobile('BMW','black')
print(pass_auto2.__class__)
print(pass_auto2.get_name())
print(pass_auto2.get_wheels())
pass_auto2.set_doors(5)
print(pass_auto2.get_doors())
pass_auto2.print_electric()
pass_auto2.beep()
