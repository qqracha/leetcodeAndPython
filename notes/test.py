from random import randint

arr = []
for i in range(10):
    arr.append(randint(1,9))
print(f'Изначальный:\n{arr}\n')

# # Bubble sort
# # def Bubble_sort(arr):
# #     x = len(arr)
# #     for i in range(x):
# #         for j in range(x - i - 1):
# #             if arr[j] > arr[j+1]:
# #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# #     return arr


# # Bubble_sort(arr)
# # max_value = ((arr[-1]-1)*(arr[-2]-1))
# # print(f'Отсортированный: {arr}')
# # print(max_value)

# def merge_sort(arr):
#     # Проверка: Если массив из 1 или 0 элемента - он уже отсортирован
#     if len(arr) <= 1:
#         return arr
#     # 1. Разделение (Divide)
#     mid = len(arr) // 2 # Делим попалам длинну массива, для нахождения середины
#     left_half = merge_sort(arr[:mid]) # Левая отсортированная половина, потому что рекурсивно вызывается merge_sort(), который сортирует половину
#     right_half = merge_sort(arr[mid:]) # Правая отсортированная половина, потому что рекурсивно вызывается merge_sort(), который сортирует половину
#     # 2. Слияние (Merge)
#     return merge(left_half, right_half) # Здесь мы обращаемся к функции merge, которая будет соединять эти 2 части

# def merge(left, right):
#     result = [] # Создаём пустой массив для дальнейшего хранения в нём отсортированного списка
#     i = j = 0 # Задаём указатели для прохождения по элементам, со стартовыми индексами "0"

#     # Сравниваем элементы из обеих половин по указателям
#     while i < len(left) and j < len(right): # Проходимся до того момента, пока не закончатся элементы в одной из половин
#         if left[i] <= right[j]:
#             result.append(left[i]) # Если Left <= Right - вставляем Left (наименьший элемент).
#             i += 1 # Идём дальше
#         else:
#             result.append(right[j]) # Если Right <= Left - вставляем Right (наименьший элемент).
#             j += 1 # Идём дальше 

#     result.extend(left[i:]) # Добавляем остаток элементов из Left половины в конец массива (если остались)
#     result.extend(right[j:]) # Добавляем остаток элементов из Right половины в конец массива (если остались)
#     return result # Возвращаем результат ( ͡° ͜ʖ ͡°)


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# print(f'Отсортированный, при помощи Merge Sort:\n{merge_sort(arr)}\n')

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(f'Отсортированный, при помощи Merge Sort:\n{merge_sort(arr)}\n')