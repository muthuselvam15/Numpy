arr = np.array([20,30,40,50,60])
print(f"Original array: {arr}")

# Basic array operations
print(f"Sum of array elements: {np.sum(arr)}")
print(f"Mean of array elements: {np.mean(arr)}")
print(f"Maximum element: {np.max(arr)}")
print(f"Minimum element: {np.min(arr)}")

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original matrix:\n{matrix}")

# Matrix operations
print(f"Sum of matrix elements: {np.sum(matrix)}")
print(f"Transpose of matrix:\n{matrix.T}")

# Element-wise operations
arr_squared = arr ** 2
print(f"Array elements squared: {arr_squared}")

# Reshaping arrays
reshaped_arr = arr.reshape(5, 1)
print(f"Reshaped array (5x1):\n{reshaped_arr}")

# Using arange and linspace
range_arr = np.arange(0, 10, 2)
print(f"Array from arange: {range_arr}")
linspace_arr = np.linspace(0, 1, 5)
print(f"Array from linspace: {linspace_arr}")
