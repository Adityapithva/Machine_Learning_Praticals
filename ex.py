import numpy as np

# Creating arrays for demonstration
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# a) add() - Adding two arrays element-wise
result_add = np.add(array1, array2)
print("Result of add():\n", result_add)

# b) stack() - Stacking two arrays along axis 0
result_stack = np.stack((array1, array2), axis=0)
print("\nResult of stack() along axis 0:\n", result_stack)

# c) reshape() - Reshaping an array to a new shape
array3 = np.array([1, 2, 3, 4, 5, 6])
result_reshape = np.reshape(array3, (2, 3))
print("\nResult of reshape() to shape (2, 3):\n", result_reshape)

# d) power() - Raising elements of an array to a specified power
result_power = np.power(array1, 2)
print("\nResult of power() (squared elements):\n", result_power)
