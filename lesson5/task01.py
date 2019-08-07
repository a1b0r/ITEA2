# Создать декоратор, который будет запускать функцию в отдельном потоке.
# Декоратор должен принимать следующие аргументы: название потока, является ли поток демоном.

from threading import Thread
import random
import time


class RandomGeneratorThread(Thread):
    def __init__(self, name, daemon):
        self._name = name
        self._daemon = bool(daemon)
        Thread.__init__(self, name=self._name)

    def run(self):
        print(f"I'm executing {self._name} with demon {self._daemon}")
        time.sleep(random.randint(0, 5))
        print(f"The end of {self._name} with demon {self._daemon}")


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        thrd = RandomGeneratorThread(args[0], args[1])
        if args[1]:
            thrd.daemon = True
        thrd.start()
        return result
    return wrapper


@decorator
def run_decorator(dec_name, dec_demon):
    pass


number_of_treads = 10

for new_thread in range(number_of_treads):
    is_daemon = random.randint(0, 1)

    run_decorator(f'Thread{new_thread}',is_daemon)
