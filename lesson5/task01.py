import random


class File:

    def __init__(self, filename, open_status):
        print("__init__")
        self._filename = filename
        self._open_status = open_status

    def __enter__(self):
        print("__enter__")
        print(f'Entered args are {self._filename, self._open_status}')
        self._f = open(self._filename, self._open_status)
        return self._f

    def __exit__(self, *args):
        print("__exit__")
        self._f.close()
        if args[0] is None:
            print(f'{args[0]}, {args[1]}, {args[2]}')

    def __del__(self):
        print("__del__")


with File('file01.txt', 'w') as file:
    print("__main__")
    for i in range(random.randint(1, 10)):
        file.write("This is line %d\r" % (i + 1))
