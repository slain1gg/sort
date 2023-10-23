import random
import time
N = [16,100,500,1000,5000]

def merge(list1, list2): # Функция слияния
    i = 0
    j = 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    while i < len(list1):
        res.append(list1[i])
        i += 1

    while j < len(list2):
        res.append(list2[j])
        j += 1

    return res


def merge_sort(a): # Сортировка Merge Sort
    mid = len(a) // 2
    L = a[:mid]
    R = a[mid:]
    if len(a) == 1:
        return a
    return merge(merge_sort(L), merge_sort(R))


def count_sort(a):
    n = len(a) # длина массива a
    res = [0 for i in range(n)] # Массив, заполненный нулями
    count = [0 for i in range(n)] # Массив, заполненный нулями
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] < a[j]:
                count[j] += 1
            else:
                count[i] += 1

    for i in range(n):
        res[count[i]] = a[i]
    a = res.copy() # Копирование из вспомогательного массива в основной
    return a

def is_correction(a): # Функция проверки на корректность сортировки
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            print(a[i], a[i+1])
            return False
    return True

for n in N:
    a = []
    with open('test.txt', 'r') as f:
        for i in range(n):
            a.append(int(f.readline()))

    #замер времени работы функций
    start_count_sort = time.time()
    count_sort(a)
    finish_count_sort = time.time()

    start_merge_sort = time.time()
    merge_sort(a)
    finish_merge_sort = time.time()

    start_quick_sort = time.time()
    sorted(a) # quick sort
    finish_quick_sort = time.time()

    print(f'Время работы функций для массива размером {n}:')
    print(f'Count sort = {(finish_count_sort-start_count_sort)*1000000} мксек')
    print(f'Merge sort = {(finish_merge_sort - start_merge_sort) * 1000000} мксек')
    print(f'Quick sort = {(finish_quick_sort - start_quick_sort) * 1000000} мксек')
    print()
    a = count_sort(a)

    if not is_correction(a):
        print('Ошибка при сортировке!')



