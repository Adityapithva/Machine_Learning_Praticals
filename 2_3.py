import numpy as np;
arr = np.array([1,2,3,4,5]);
print("Array before appending:",arr);
values_to_append = [5,6,7];
new_arr = np.append(arr, values_to_append);
print("Array after appending:",new_arr);
