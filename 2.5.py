# from random import randrange
# n = int(input())
# m = int(input())
# results = [1 if [randrange(0, 2) for i in range(3)].count(1) == 2 else 0 for _ in range(1000000)]
# print(f'{round(results.count(1) / len(results) * 100, 1)}%')
from numpy.random import choice
from numpy import round, sum
# n = int(input())
# m = int(input())

n = 3
m = 2

r = choice([0, 1], size=(10000000, n))
# print(f"{round(sum(sum(r, axis=1) == m) / len(r) * 100, 1)}%")
print(f'{round(sum(sum(r, axis=1) <= m)/len(r) * 100, 1)}%')
