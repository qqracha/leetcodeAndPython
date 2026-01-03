# class Square:
#     def __init__(self, side = 2):
#         self.side = side
#
#     @property
#     def area(self):
#         return self.side ** 2
#
#     def __str__(self):
#         return f"Квадрат со стороной {self.side} имеет площадь {self.area}"
#
#     def __repr__(self):
#         return f"Значения квадрата:\nside = {self.side}"
#
# class Rectangle(Square):
#     def __init__(self, side = 2, length = 5):
#         super().__init__(side)
#         self.length = length
#
#     @property
#     def area(self):
#         return self.side * self.length
#
#     def __str__(self):
#         return f"Прямоугольника со стороной от квадрата {self.side} и шириной {self.length} имеет площадь {self.area}"
#
#     def __repr__(self):
#         return f"Значения прямоугольника:\nside = {self.side} (Наследование от квадрата)\nlength = {self.length}"
#
#
# lysis = Square()
# user_lysis = Square(4)
#
# enigma = Rectangle()
# user_enigma = Rectangle(4)
#
# print("." * 75)
# print(user_lysis, repr(lysis), sep="\n")
#
# print(user_enigma, repr(enigma), sep="\n")
from fontTools.misc.cython import returns

x = {1: "Apple", 2: "Pineapple", 3: "Cherry"}

try:
    # print(x.get(4))
    result = 1 / 0
except ZeroDivisionError:
    print("Ошибка синтаксиса")
except Exception:
    print("Какая-то ошибка")