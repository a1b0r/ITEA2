
class NumberGenerator:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start

        raise StopIteration('The end of structure')


a = NumberGenerator(0, 3)

print(iter(a))

print(next(a))
print(next(a))
print(next(a))

print('='*5)

b = NumberGenerator(0, 3)

for i in b:
    print(i)
