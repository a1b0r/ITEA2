class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super.__new__(cls)

            return cls._instance


class A:
    pass


var_list = [1, 2, 3]
print(type(var_list))
print(type(A))
print(type(A()))