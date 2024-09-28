import numpy as np
array = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
rows = np.mean(array, axis=1)
columns = np.mean(array, axis=0)
print("Mean across rows:",rows)
print("Mean across columns:",columns)
