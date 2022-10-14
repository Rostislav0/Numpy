import numpy as np

np.random.seed(42)
# Z = np.random.random_sample(list(map(int, input().split())))
# print(Z)

# Z = np.random.random_sample(list(map(int, input().split())))
# print(np.min(Z))
# print(np.max(Z))

# Z = np.random.random_sample(list(map(int, input().split())))
# print(np.average(Z))

Z = np.random.random_sample(list(map(int, input().split()))).mean(axis=0)
print(Z.min())
print(Z.max())