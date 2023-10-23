import random
N = 5000

with open('test.txt', 'w') as f:
  for _ in range(N):
    f.write(f"{random.randint(100, 1000)}\n")