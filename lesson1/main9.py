def check(n):
    try:
        a = n/1
        return 100
    except ZeroDivisionError:
        pass
    finally:
        return 200

print(check(10))