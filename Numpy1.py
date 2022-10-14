# 1 Numpy
import numpy as np

M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))
M2 = np.copy(M1)
M2[-2] = np.around((np.sin(M1[-2]*np.pi/6)), 2)
M2[:, -2] = np.around(np.e ** M1[:, -2], 2)
M2[-2][-2] = np.around(np.e ** np.sin(M1[-2][-2]*np.pi/6), 2)
print(M1)
print(M2)
print(M2[:, -2])
print()
print(M1[:, -2])


def Z(y, x=1, z=float):
    return np.zeros((x, y), dtype=z)


print(Z(input()))

