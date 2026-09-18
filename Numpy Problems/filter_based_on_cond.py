import numpy as np
arr = np.array([5, 12, 29, 30, 44, 7, 18])
filter_arr = arr[arr < 30]
print(filter_arr)