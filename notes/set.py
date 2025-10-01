import sys
from contextlib import redirect_stdout

class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, text):
        for f in self.files:
            f.write(text)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

output_file = "output.txt"

with open(output_file, "w") as f, redirect_stdout(Tee(sys.__stdout__, f)):
    s = list(set([1, 1, 2, 2, 3, 6, 4, 5]))
    print(f"Input list: {[1, 1, 2, 2, 3, 6, 4, 5]}\n")
    print(f"Expression list(set([])): {s}") # не гарантирует сохранение исходного порядка элементов (сортирует массив)

    lst = [1, 1, 2, 2, 3, 6, 4, 5]
    unique_lst = list(dict.fromkeys(lst)) # гарантирует сохранение исходного порядка элементов
    print(f"Expression list(dict.fromkeys()): {unique_lst}")  # [1, 2, 3, 6, 4, 5]

    res = []
    for x in [1, 1, 2, 2, 3, 6, 4, 5]: # добавляет только уникальные значения в массив, при этом сохраняет исходный порядок (не сортирует)
        if x not in res:
            res.append(x)
    print(f"Expression 'Explicit iterative deduplication': {res}")

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("----------")
    print(f"Input set A: {a}")
    print(f"Input set B: {b}\n")
    print(f"Union A | b: {a | b}")  # {1, 2, 3, 4, 5, 6}  — объединение
    print(f"Intersection A & B: {a & b}")  # {3, 4}             — пересечение
    print(f"Difference A - B: {a - b}")  # {1, 2}             — разность
    print(f"Symmetric_difference A ^ B: {a ^ b}")  # {1, 2, 5, 6}       — симметрическая разность
    print("-----------")

    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}

    print(f"Input set A: {a}")
    print(f"Input set B: {b}\n")
    print(f"B is subset A: {b.issubset(a)}") # False
    print(f"A is subset B: {a.issubset(b)}") # True
    print(f"B is superset A: {b.issuperset(a)}") # True
    print(f"A is superset B: {a.issuperset(b)}") # False
    print(f"A is disjoint B: {a.isdisjoint(b)}") # False
    print("-----------")

    a.update(b)
    print(f"Updated a from b: {a}")

    s = {1, 2, 3, 4}
    t = {3, 4, 5, 6}

    s.intersection_update(t)
    print(f"Intersection_update s & t: {s}") # {3,4}
    sys.stdout = sys.__stdout__ 

print(f"File {output_file} was updated")
