import numpy as np
A = np.array([[4, 2],
              [1, 3]])
eigval, eigvecs = np.linalg.eig(A)
print(eigval)
print(eigvecs)