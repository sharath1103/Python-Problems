import numpy as np
a = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(a).any())