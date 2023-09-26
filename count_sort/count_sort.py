import random
import time
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
    
a = [random.randint(100,1000) for i in range(5000)]
s = time.time()
count_sort(a)
f = time.time()
print((f-s)*1000)
