class File:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __enter__(self):
        print(f'Entered args are {self._a, self._b}')
        return 'Hello'

    def __exit__(self, *args):
        print('The end of context manager')
        print(args)


with File(1, 2) as f:
    print(f)
    print(1/0)