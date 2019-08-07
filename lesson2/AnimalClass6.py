class Animal:

    name = 'name'
    animal_type = None
    animals_created = 0

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        Animal.animals_created += 1

    def move(self):
        print("I'm moving")

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")

    def who_am_i(self):
        print("I'm the {0}. My type is {1}".format(self.name, self.animal_type))


animal_object = Animal('Human','mammal')
animal_object1 = Animal('Human','mammal')
print(Animal.animals_created)

