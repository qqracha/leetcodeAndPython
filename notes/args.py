# Args & Kwargs - именнованные и неименованные аргументы, при помощи которых можно создавать фукнции, которые принимают 
# количество аргументов

def greet(*args): # *args - в кортеж
    print(args)

greet("i", "wanna", "pizza")

def my_sum(*args):
    return sum(args)

print(my_sum(1, 2))           # 3
print(my_sum(1, 2, 3, 4, 5))  # 15


def info(**kwargs): # **kwargs - в словарь
    print(kwargs)

info(name = "Даша", age = 20)