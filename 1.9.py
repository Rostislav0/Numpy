import numpy as np

start = int(input())
stop = int(input())
n = int(input())

Z = np.round(np.geomspace(start, stop, n), 3)
print(Z)
