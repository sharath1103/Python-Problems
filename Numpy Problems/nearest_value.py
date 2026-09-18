import numpy as np
arr = np.array([1.5, 2.8, 3.2, 4.1])
target_value = 3
index = np.abs(arr - target_value).argmin()
nearest_value = arr[index]
print(f"The value closest to {target_value} is: {nearest_value}")