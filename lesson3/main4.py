def decorator(func):
    def wrapper(*args, **kwargs):
        print('The begin of wrapper')
        result = func()
        print('The end of wrapper')
        return result
    return wrapper


@decorator
def hi():
    print('hello')

print(hi)