import numpy as np

# Z = np.arange(11)
# Z[(Z > 3) & (Z < 9)] *= -1
# print(Z)

# A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
# A[(A < 0)] = np.floor(A[(A < 0)])
# A[(A > 0)] = np.ceil(A[(A > 0)])
# Z = A
# print(Z)


# equals values in two arrays
A = np.arange(-5, 5)
B = np.array([9, -5, 2])
print(np.intersect1d(A, B))

A = np.array([1, 2, 3, 4, 5])
B = np.array([-5, -4, -3])
print(np.intersect1d(A, B))

A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])
print(np.intersect1d(A, B))

print(np.array([*set(A).intersection(set(B))]))
