import numpy as np
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
sorted_indices = sampleArray[:,1].argsort()
sorted_array = sampleArray[sorted_indices]
print(sorted_array)