import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumnToAdd = np.array([10, 10, 10])
deletedArray = np.delete(sampleArray, 1, axis=1)
resultArray = np.insert(deletedArray, 1, newColumnToAdd, axis=1)
print(resultArray)