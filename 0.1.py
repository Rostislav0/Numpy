import numpy as np


def Prin(z=float, *args):
    args = list(args)
    if z.isdigit():
        args.append(z)
        z = float
    x = []
    for i in args:
        x.append(int(i))
    return np.zeros(shape=x[::-1], dtype=z)


Z = Prin(*input().split()[::-1])
print(Z)

# 2 methods
args = input().split()

try:
    Z = np.zeros(tuple(map(int, args)))
except ValueError:
    Z = np.zeros(tuple(map(int, args[:-1])), args[-1])

print(Z)
