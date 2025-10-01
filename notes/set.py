s = list(set([1,1,2,2,3,6,4,5]))
print(s) # не гарантирует сохранение исходного порядка элементов (сортирует массив)

lst = [1, 1, 2, 2, 3, 6, 4, 5]
unique_lst = list(dict.fromkeys(lst)) # гарантирует сохранение исходного порядка элементов
print(unique_lst)  # [1, 2, 3, 6, 4, 5]

res = []
for x in [1, 2, 8, 2, 2, 3, 3, 1]: # добавляет только уникальные значения в массив, при этом сохраняет исходный порядок (не сортирует)
    if x not in res:
        res.append(x)
print(res)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("----------")
print(a | b)  # {1, 2, 3, 4, 5, 6}  — объединение
print(a & b)  # {3, 4}             — пересечение
print(a - b)  # {1, 2}             — разность
print(a ^ b)  # {1, 2, 5, 6}       — симметрическая разность


a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))   # True
print(b.issuperset(a)) # True
print(a.isdisjoint(b)) # False
print(b.issubset(a)) # False
print(a.issubset(b)) # True
print(b.issuperset(a)) # True
print(a.issuperset(b)) # False

a.update(b)
print(a)
a.intersection_update(b)
print(a)