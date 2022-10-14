import numpy as np

V = {1: 2, 3: 4}
V = range(10)
V = map(np.sin, range(10))
print(np.fromiter(V, dtype=float))  # == Z = np.array(list(V), dtype=float)
