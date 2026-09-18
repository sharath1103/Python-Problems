import numpy as np
arr = np.random.randint(1,51,size=(3,3))
print(arr)
sorted_arr = np.sort(arr,axis=1)
print(sorted_arr)