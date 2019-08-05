list_var = [(1, 2), (3, 4), (5, 6), (7, 8)]

new_list = [tuple(x ** 2, y ** 2) if not x % 2 else (x * (-1), y ** 2) for x, y in list_var]

print(new_list)