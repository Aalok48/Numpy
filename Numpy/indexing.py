import numpy as np

# indexing in array is same in python as list
# in case of two dimension array such as 2*2 square matrix, the first row is 0 and second row is 1 while in first row first element is 0 and second element is 1

# Example for 1d array
arr1 = np.array([1, 2, 3])
print(arr1[1])     # this is an example of array indexing... this gives output 2 as it is in place of 1
print(arr1[0:2])   # this is an example of array slicing
print()

# Example for 2d array
arr2 = np.array([[2,4,6],[7,8,9]])
print(arr2[0,1])   # the first attribute is for the first row and the second attribute is for the element index
print(arr2[1,-1])  # negative indexing can also be used for array indexing but it works from last element
print()

# Example for 3d array
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3[0,1,1])