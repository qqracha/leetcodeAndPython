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
# # print(user_enigma, repr(enigma), sep="\n")
# from PyQt5.QtCore.QUrl import kwargs
# from fontTools.misc.cython import returns
# from win11toast import result
from telethon.crypto.libssl import encrypt_ige

# x = {1: "Apple", 2: "Pineapple", 3: "Cherry"}
#
# try:
#     # print(x.get(4))
#     result = 1 / 0
# except ZeroDivisionError:
#     print("Ошибка синтаксиса")
# except Exception:
#     print("Какая-то ошибка")

# import random
#
# from youtube_dl.utils import limit_length
#
# x = ["Gena", "Nicola", "Egor", "Sasha"]
#
# def repeat(num_times): # Внешний слой принимает те параметры, которые будут у декоратора.
#     def decorator(func): # Средний слой получает саму функцию как объект
#         def wrapper(*args, **kwargs): # Внутренний слой является заменой оригинальной функции
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(num_times=5)
# def choose(name):
#     print(f"Привет {name}, сегодня на твоём пути будет - {random.choice(x)}")

# choose("Misa")

x = [9,2,8,4,5,6]

# Итератор
class Enigma:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        raise StopIteration

# Генератор
def rogen(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

enigma_test = Enigma(len(x))
for i in enigma_test:
    print(f"Элемент из списка: {x[i-1]}")

print("-"*20)

rogen_test = rogen(len(x))
for i in rogen_test:
    print(f"Скибоб: {x[i-1]}")

y = list(set(x))
print(y)