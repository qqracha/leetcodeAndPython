"""
Все типы данных в Python:

int, float, complex, str, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType, slice, function, type, object, module, ellipsis
"""


# ============= ЧИСЛОВЫЕ ТИПЫ =============

# 1. int (целые числа)
integer_num = 42
print(f"int: {integer_num}, тип: {type(integer_num)}")

# 2. float (числа с плавающей точкой)
float_num = 3.14159
print(f"float: {float_num}, тип: {type(float_num)}")

# 3. complex (комплексные числа)
complex_num = 3 + 5j
print(f"complex: {complex_num}, тип: {type(complex_num)}")


# ============= ПОСЛЕДОВАТЕЛЬНОСТИ =============

# 4. list (список - изменяемый)
my_list = [1, 2, 3, "текст", True]
print(f"list: {my_list}, тип: {type(my_list)}")

# 5. tuple (кортеж - неизменяемый)
my_tuple = (1, 2, 3, "текст", False)
print(f"tuple: {my_tuple}, тип: {type(my_tuple)}")

# 6. range (диапазон)
my_range = range(0, 10, 2)
print(f"range: {list(my_range)}, тип: {type(my_range)}")


# ============= ТЕКСТОВЫЕ ТИПЫ =============

# 7. str (строка)
my_string = "Привет, мир!"
print(f"str: {my_string}, тип: {type(my_string)}")


# ============= БИНАРНЫЕ ТИПЫ =============

# 8. bytes (байты - неизменяемые)
my_bytes = b"Hello"
print(f"bytes: {my_bytes}, тип: {type(my_bytes)}")

# 9. bytearray (массив байтов - изменяемый)
my_bytearray = bytearray(b"Hello")
print(f"bytearray: {my_bytearray}, тип: {type(my_bytearray)}")

# 10. memoryview (представление памяти)
my_memoryview = memoryview(bytes(5))
print(f"memoryview: {my_memoryview}, тип: {type(my_memoryview)}")


# ============= МНОЖЕСТВА =============

# 11. set (множество - изменяемое)
my_set = {1, 2, 3, 4, 5}
print(f"set: {my_set}, тип: {type(my_set)}")

# 12. frozenset (замороженное множество - неизменяемое)
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(f"frozenset: {my_frozenset}, тип: {type(my_frozenset)}")


# ============= СЛОВАРИ =============

# 13. dict (словарь)
my_dict = {"имя": "Иван", "возраст": 30, "город": "Москва"}
print(f"dict: {my_dict}, тип: {type(my_dict)}")


# ============= БУЛЕВЫ ЗНАЧЕНИЯ =============

# 14. bool (булев тип)
is_true = True
is_false = False
print(f"bool (True): {is_true}, тип: {type(is_true)}")
print(f"bool (False): {is_false}, тип: {type(is_false)}")


# ============= NONE ТИП =============

# 15. NoneType (отсутствие значения)
none_value = None
print(f"NoneType: {none_value}, тип: {type(none_value)}")


# ============= ДОПОЛНИТЕЛЬНЫЕ ТИПЫ =============

# 16. slice (срез)
my_slice = slice(1, -1)
print(f"slice: {my_slice}, тип: {type(my_slice)}")
# Применение среза
x = [1, 2, 3, 4, 5]
print(f"Применение среза: {x[my_slice]}")

# 17. function (функция)
def my_function():
    return "Это функция"

print(f"function: {my_function}, тип: {type(my_function)}")

# 18. class (класс)
class MyClass:
    pass

print(f"class: {MyClass}, тип: {type(MyClass)}")

# 19. object instance (экземпляр класса)
my_object = MyClass()
print(f"object instance: {my_object}, тип: {type(my_object)}")

# 20. module (модуль)
import math
print(f"module: {math}, тип: {type(math)}")


# ============= ПРОВЕРКА ТИПОВ =============

print("\n" + "="*50)
print("ПРОВЕРКА ТИПОВ С isinstance():")
print("="*50)

print(f"42 это int? {isinstance(42, int)}")
print(f"3.14 это float? {isinstance(3.14, float)}")
print(f"'текст' это str? {isinstance('текст', str)}")
print(f"[1,2,3] это list? {isinstance([1,2,3], list)}")
print(f"True это bool? {isinstance(True, bool)}")


# ============= ПРЕОБРАЗОВАНИЕ ТИПОВ =============

print("\n" + "="*50)
print("ПРИМЕРЫ ПРЕОБРАЗОВАНИЯ ТИПОВ:")
print("="*50)

# Преобразование в int
print(f"int('123') = {int('123')}")
print(f"int(3.14) = {int(3.14)}")

# Преобразование в float
print(f"float('3.14') = {float('3.14')}")
print(f"float(5) = {float(5)}")

# Преобразование в str
print(f"str(123) = {str(123)}")
print(f"str([1,2,3]) = {str([1,2,3])}")

# Преобразование в list
print(f"list('abc') = {list('abc')}")
print(f"list((1,2,3)) = {list((1,2,3))}")

# Преобразование в tuple
print(f"tuple([1,2,3]) = {tuple([1,2,3])}")

# Преобразование в set
print(f"set([1,1,2,2,3]) = {set([1,1,2,2,3])}")
