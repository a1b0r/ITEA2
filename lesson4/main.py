my_var = list()
print(type(my_var))
print(type(type(my_var)))


class A:
    pass

B = type("MyNewClass", (), {"var_in_class": "yes"})

print(A)
print(B)
print(B.var_in_class)

print(B.__dict__)

b = B()
print(b.__dict__)

b.new_var = 100
print(b.__dict__)