class Point:
    __slots__ = ('x','y') # Явное разрешение определённых полей

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10,20)
print(p.x) # 10

try:
    p.z = 30
except AttributeError:
    print("Ошибка: нельзя добавлять новые поля")