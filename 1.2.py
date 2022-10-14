import numpy as np


def check(a, b):
    try:
        z = np.dot(a, b)
    except ValueError:
        z = 'Упс! Что-то пошло не так...'
    return z


A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [11.5, 12.5, 13.5]
])

print(check(A, B))

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [11.5],
    [12.5],
    [13.5]
])

print(check(A, B))
