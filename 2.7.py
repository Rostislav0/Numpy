from numpy.random import choice
from numpy import arange, stack, sum, round, max

L = int(input())  # 100, 100
M = int(input())  # 80, 10

r = choice(arange(0.1, L, .1), size=(1000000, 1))
r_s = stack([r, L - r])
r_s = max(r_s, axis=0)
print(f'{round(sum(r_s >= M) / len(r) * 100, 1)}%')
