import numpy as np;
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
mean_value = np.mean(arr, axis=1)
std_dev = np.std(arr, axis=1);
variance = np.var(arr, axis=1);

print("Mean along axis 1:", mean_value);
print("Standard deviation along axis 1:", std_dev);
print("Variance along axis 1:", variance);
