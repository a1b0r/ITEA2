def hello_world():
    print('hello world')


def devision(func, arg1, arg2):
    try:
        func()
        result = arg1 / arg2
        print(result)
    except ZeroDivisionError:
        print('Inside except block')


devision(hello_world, 10, 20)
