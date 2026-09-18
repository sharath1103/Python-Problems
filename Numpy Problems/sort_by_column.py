import numpy as np
arr = np.array([[8, 4, 1],
                [5, 2, 7],
                [6, 9, 3]])
sorted_index = arr[:,1].argsort()
sorted_array = arr[sorted_index]
print(sorted_array)