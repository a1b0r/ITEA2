
def number_generator(numbers):

    for i in range(numbers):
        yield i
        print(f'After first yield')
        yield i
        print(f'After second yield')


a = number_generator(10)

next(a)
next(a)
next(a)
next(a)
print('='*5)
for i in number_generator(10):
    pass
