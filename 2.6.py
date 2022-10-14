from numpy.random import choice
from numpy import round, sum

# n = int(input())
# m = int(input())
# k = int(input())
n = 2
m = 6
k = 7

r = choice(range(1, m + 1), size=(10000000, n))
print(f"{round(sum(sum(r, axis=1) >= k) / len(r) * 100, 1)}%")

# print(f'{round(sum(sum(r, axis=1) <= m)/len(r) * 100, 1)}%')
