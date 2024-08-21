import numpy as np
arr = np.array([50, 45, 60, 55, 70])

new = np.diff(arr)

print("Original Array:", arr)
print("Difference between neighboring elements:", new)
