import numpy as np

# Sample Input 2:
#
# -1
# 0
# 9
# Sample Output 2:
#
# [-0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1]


start = int(input())
stop = int(input())
n = int(input())

Z = np.round(np.linspace(start, stop, n+1, endpoint=False), 3)[1:]
print(Z)
