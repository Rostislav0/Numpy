import numpy as np
n = int(input())
rand = np.random.randn(1000000, n).argsort(axis=1)
print(f'{np.round(np.sum(np.any(rand == np.arange(n), axis=1)) / len(rand) * 100, 1)}%')

