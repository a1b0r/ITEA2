
def number_generator(numbers):

    for i in range(numbers):
        yield i


a = number_generator(10)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))