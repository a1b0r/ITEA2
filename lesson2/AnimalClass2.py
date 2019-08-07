class Animal:
    name = None
    animal_type = None

    def move(self):
        print("I'm moving")

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")

    def who_am_i(self):
        print("I'm the {0}. My type is {1}".format(self.name, self.animal_type))


animal_object = Animal()
print(animal_object.__sizeof__())

animal_object.eat()
animal_object.sleep()
animal_object.move()

animal_object.name = 'Human'
animal_object.animal_type = 'mammal'
animal_object.who_am_i()

