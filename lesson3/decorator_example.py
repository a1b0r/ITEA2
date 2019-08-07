def decorator(func):
    def wrapper(*args, **kwargs):
        print('The begin of wrapper')
        result = func()
        print('The end of wrapper')
        return result
    return wrapper()


def hi():
    print('hello')


a = decorator(hi)
print(a)