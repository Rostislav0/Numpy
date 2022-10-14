import numpy as np
x = int(input())
y = int(input())
Z = np.zeros(shape=y+1 - x, dtype=int)
for i in range(len(Z)):
    Z[i] = x
    x += 1

Z = np.arange(int(input()), int(input()) + 1)
print(Z)