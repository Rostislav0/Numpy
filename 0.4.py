import numpy as np

x = int(input())
b = input().split()
m = 0
Z = np.zeros(shape=(int(b[0]), int(b[1])), dtype=int)

for i in range(len(Z)):
    for c in range(len(Z[i])):
        Z[i][c] = m
        m += 1

print(Z)

a = np.arange(int(input())).reshape([int(i) for i in input().split()])
print(a)
