print(__name__)

print(globals())
print(locals())


def check_locals():
    a = 0
    b ="q"
    print(locals())


check_locals()