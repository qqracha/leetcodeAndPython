"""Атрибут класса можно удалять при помощи del."""

class mycls():
    x = 1

print(mycls.x) # 1
del mycls.x
print(mycls.x) # AttributeError: type object 'mycls' has no attribute 'x'