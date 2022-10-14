import numpy as np

# Sample Input 2:
#
# 5 4
#  -5
# Sample Output 2:
#
# [[-5. -5. -5. -5.]
#  [-4. -4. -4. -4.]
#  [-3. -3. -3. -3.]
#  [-2. -2. -2. -2.]
#  [-1. -1. -1. -1.]]

n, m = map(int, input().split())
k = int(input())
Z = np.array([np.arange(k, k + n)] * m, dtype=float).T
print(Z)
