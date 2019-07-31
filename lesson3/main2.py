# 79 in one line


def a(b):
    def b(c):
        print(c)

        def e(f):
            return 'The end'
        return e
    return b


result = a(10)(29)(10)
print(result)