try:
    k = 1/0
except:
    print('Exception was caught')

print('-'*5)
try:
    k = 1/0
except ZeroDivisionError:
    print('Zero Division is not allowed')
except KeyError:
    print('KeyError was caught')

print('-'*5)
try:
    k = ['key']
except ZeroDivisionError:
    print('Zero Division is not allowed')
except KeyError:
    print('KeyError was caught')

print('-'*5)
try:
    k = ['key']
except (ZeroDivisionError, KeyError) as e:
    print(e)

print('-'*5)
try:
    k = ['key']
except (ZeroDivisionError, KeyError) as e:
    print(e)