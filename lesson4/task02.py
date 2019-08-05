from abc import ABC, abstractmethod


class Persona(ABC):

    @abstractmethod
    def show_all_information(self):
        pass

    @abstractmethod
    def show_actual_age(self):
        pass


class Student(Persona):

    def show_all_information(self):
        super().show_all_information()

    def show_actual_age(self):
        super().show_actual_age()


