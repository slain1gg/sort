import random
import time
N = 500
with open('test.txt', 'w') as f:
  for _ in range(N):
    f.write(f"{random.randint(100, 1000)}\n")


def count_sort(a):
  n = len(a)
  res = [0 for i in range(n)]
  count = [0 for i in range(n)]
  for i in range(n):
    for j in range(i + 1, n):
      if a[i] < a[j]:
        count[j] += 1
      else:
        count[i] += 1

  for i in range(n):
    res[count[i]] = a[i]
  a = res.copy()
  return a


a = []
with open('test.txt', 'r') as f:
  for i in range(N):
    a.append(int(f.readline()))



start = time.time()
count_sort(a)
finish = time.time()
print((finish - start)*1000000)

# todo: реализовать сортировку слиянием, построить график, сравнить

#Проверка функции на корректность

if count_sort(a) != sorted(a):
  print('ERROR')
else:
  print('Все хорошо')
