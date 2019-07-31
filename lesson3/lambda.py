addition = lambda x, y: x + y
print(addition(1,3))

# map, filter()

list_var = [0,100, -100, 25, 34, -2, -5]

map_var = map(lambda x: x ** 2, list_var)
print(map_var)
map_var = list(map_var)
print(map_var)

map_var = filter(lambda x: x > 0, list_var)
print(map_var)
map_var = list(map_var)
print(map_var)
