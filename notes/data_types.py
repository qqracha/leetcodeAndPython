"""
Все типы данных в Python:

int, float, complex, str, list, tuple, range, dict, set, frozenset, bool, bytes, 
bytearray, memoryview, NoneType, slice, function, type, object, module, ellipsis
"""

integer_num = 42 # int (целые числа)

float_num = 3.14159 # float (числа с плавающей точкой)

complex_num = 3 + 5j # complex (комплексные числа)

my_list = [1, 2, 3, "текст", True] # list (список - изменяемый)

my_tuple = (1, 2, 3, "текст", False) # tuple (кортеж - неизменяемый)

my_range = range(0, 10, 2) # range (диапазон)

my_string = "Привет, мир!" # str (строка)

my_bytes = b"Hello" # bytes (байты - неизменяемые)

my_bytearray = bytearray(b"Hello") # bytearray (массив байтов - изменяемый)

my_memoryview = memoryview(bytes(5)) # memoryview (представление памяти)

my_set = {1, 2, 3, 4, 5} # set (множество - изменяемое)

my_frozenset = frozenset([1, 2, 3, 4, 5]) # frozenset (замороженное множество - неизменяемое)

my_dict = {"имя": "Иван", "возраст": 30, "город": "Москва"} # dict (словарь)
empty_dict = {} # dict (и это словарь)

is_true = True # bool (булев тип)
is_false = False # bool (булев тип)

none_value = None # NoneType (отсутствие значения)

my_slice = slice(1, -1) # slice (срез)
x = [1, 2, 3, 4, 5] # Применение среза

def my_function(): # function (функция)
    return "Это функция"

class MyClass: # class (класс)
    pass

my_object = MyClass() # object instance (экземпляр класса)

import math # module (модуль)

# Вывод всех типов
print(f"int: {integer_num}, тип: {type(integer_num)}")
print(f"float: {float_num}, тип: {type(float_num)}")
print(f"complex: {complex_num}, тип: {type(complex_num)}")
print(f"list: {my_list}, тип: {type(my_list)}")
print(f"tuple: {my_tuple}, тип: {type(my_tuple)}")
print(f"range: {list(my_range)}, тип: {type(my_range)}")
print(f"str: {my_string}, тип: {type(my_string)}")
print(f"bytes: {my_bytes}, тип: {type(my_bytes)}")
print(f"bytearray: {my_bytearray}, тип: {type(my_bytearray)}")
print(f"memoryview: {my_memoryview}, тип: {type(my_memoryview)}")
print(f"set: {my_set}, тип: {type(my_set)}")
print(f"frozenset: {my_frozenset}, тип: {type(my_frozenset)}")
print(f"dict: {my_dict}, тип: {type(my_dict)}")
print(f"dict: {empty_dict}, тип: {type(empty_dict)}")
print(f"bool (True): {is_true}, тип: {type(is_true)}")
print(f"bool (False): {is_false}, тип: {type(is_false)}")
print(f"NoneType: {none_value}, тип: {type(none_value)}")
print(f"slice: {my_slice}, тип: {type(my_slice)}")
print(f"Применение среза: {x[my_slice]}")
print(f"function: {my_function}, тип: {type(my_function)}")
print(f"class: {MyClass}, тип: {type(MyClass)}")
print(f"object instance: {my_object}, тип: {type(my_object)}")
print(f"module: {math}, тип: {type(math)}")
