import numpy as np

# Sample Input 2:
#
# 5 4
#  -5
# Sample Output 2:
#
# [[-5. -4. -3. -2.]
#  [-5. -4. -3. -2.]
#  [-5. -4. -3. -2.]
#  [-5. -4. -3. -2.]
#  [-5. -4. -3. -2.]]

n, m = map(int, input().split())
k = int(input())
Z = np.array([np.arange(k, k + m)] * n, dtype=float)
print(Z)
