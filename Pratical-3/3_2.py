import numpy as np;

arr1 = np.arange(1,5);
arr2 = np.arange(5,9);
new = np.hstack([arr1,arr2]);
print(new);