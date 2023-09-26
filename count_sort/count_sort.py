import random

def count_sort(a):
    n = len(a)
    res = [0 for i in range(n)]
    count = [0 for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if a[i] < a[j]:
                count[j] += 1
            else:
                count[i] += 1

    for i in range(n):
        res[count[i]] = a[i]
        
    return res

for i in range(10):
    a = [random.randint(-100,100) for i in range(10)]
    if count_sort(a) != sorted(a):
        print('ERROR')
