import random


class File:

    def __init__(self, filename, num_of_lines):
        self._filename = filename
        self._num_of_lines = num_of_lines

    def __enter__(self):
        print(f'Entered args are {self._filename, self._num_of_lines}')
        return self

    def __exit__(self, *args):
        print('The end of context manager')
        print(args)

    def open(self):
        with open(self._filename, 'w') as f:
            for l in range(self._num_of_lines):
                f.write((str(random.randint(0, 5000)) + '\n'))


file = File('file01.txt',10)

file.open()
