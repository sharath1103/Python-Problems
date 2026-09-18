import numpy as np

a = np.array([1, 2, 3, 5, 7])
b = np.array([3, 4, 5, 6, 7])

i = np.intersect1d(a,b)
u = np.union1d(a,b)

print(i)
print(u)