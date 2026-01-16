from random import randint

a = []
for i in range(10):
    a.append(randint(1,9))
print(f'Изначальный: {a}')

def bubble_sort(a):
    n = len(a)
    for i in range(2):
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

bubble_sort(a)

max_value = ((a[-1]-1)*(a[-2]-1))
print(f'Отсортированный: {a}')
print(max_value)