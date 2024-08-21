import numpy as np;
arr = np.array([
    [1,2],
    [3,4],
    [5,6]
]);
print("Array before conversion:",arr);
new_arr = arr.reshape(2,3);
print("Array after conversion:",new_arr);