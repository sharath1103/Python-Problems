import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v = np.vstack((a,b))
print(v)

h = np.hstack((a,b))
print(h)