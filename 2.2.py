import numpy

s1 = [float(i) for i in input().split()]
s2 = [float(i) for i in input().split()]
M1 = numpy.array([s1[0:2], s2[0:2]])
v1 = numpy.array([s1[2], s2[2]])
r = numpy.linalg.solve(M1, v1)
print(r[0], r[1])
