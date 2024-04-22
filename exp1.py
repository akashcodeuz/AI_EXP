#experiment for numpy 
import numpy as np
# Creating a NumPy array
arr = np.array([[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]])
 
# Printing the array
print("Array:")
print(arr)
# Basic characteristics
print("\nBasic Characteristics:")
print("Shape:", arr.shape) 
print("Size:", arr.size) 
print("Dimensions:", arr.ndim) 
print("Data Type:", arr.dtype) 
# Accessing elements
print("\nAccessing Elements:")
print("Element at (0,0):", arr[0, 0]) 
print("First Row:", arr[0]) 
print("Second Column:", arr[:, 1])