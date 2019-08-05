class Dec1:

    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        print('Start decorating')
        self._f()
        print('End decorating')


@Dec1
def hi():
    print('Say hello')

hi()