def decorator(number_of_repeats):
    print(number_of_repeats)

    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            for i in range(number_of_repeats):
                print('The begin of wrapper')
                result = func(*args, **kwargs)
                print('The end of wrapper')
            return result, func.__name__
        return wrapper
    return actual_decorator


@decorator(10)
def addition(arg1, arg2):
    return arg1 + arg2


print(addition(1,2))

