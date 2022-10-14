import numpy as np

x = int(input())
M = np.array([input().split() for i in range(x)], dtype=float)

M1 = M[:, :-1]
v1 = M[:, -1]

if np.linalg.det(M1) != 0:
    print(*np.linalg.solve(M1, v1))
else:
    print('Матрица системы вырожденная')
