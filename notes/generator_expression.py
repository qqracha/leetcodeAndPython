"""
Строка <generator object <genexpr> at 0x103f2d230> показывает:​
 - generator object — тип объекта (генератор).
 - <genexpr> — указывает, что это генераторное выражение.
 - 0x103f2d230 — адрес объекта в памяти.
Print выведет generator expression, а не tuple comprehension.
"""

x = (i**2 for i in range(4))
print(x)