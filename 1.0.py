import numpy as np
x_k = input().split()
Z = np.diag(np.arange(1, int(x_k[1])+1), k=int(x_k[0]))
print(Z)