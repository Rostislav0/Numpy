import numpy as np

L = int(input())  # 100
N = int(input())  # 2
M = int(input())  # 80

y = np.random.uniform(0, L, size=(10000000, N - 1))
x = np.insert(y, 0, values=L, axis=1)
y = np.insert(y, 0, values=0, axis=1)
x = np.sort(x)
y = np.sort(y)
z = x - y
z2 = np.max(z, axis=1)
print(f'{np.around(np.sum(z2 > M) / len(z2) * 100, 1)}%')