from abc import ABC, abstractmethod


class BaseCar(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        print("STOP")


class Car(BaseCar):
    def __init__(self):
        self.__engine = "V8"

    def move(self):
        super().move()
        print("MOVE")

    def stop(self):
        super().stop()


a = Car()
a.move()
a.stop()