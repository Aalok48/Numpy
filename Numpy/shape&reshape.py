import numpy as np

''' the shape and reshape function in numpy are two related functions. The shape() returns the rows and columns of the array whereas the reshape() function changes the array from one dimension to another '''


# arr1 = np.array([[1,2,3,4],[1,2,3,4]])
# print(arr1)
# print()
# print(arr1.ndim)   # this gives the dimension of the array
# print(arr1.shape)  # this gives the shape i.e. row and column of the array

# arr2 = np.array([1,2,3,4], ndmin=4)
# print(arr2)      # this is a 4d array and the shape is (1,1,1,4) because there is three row and four column
# print(arr2.shape)   

# reshape() function is used to convert array from one dimension to another 
# arr3 = np.array([1,2,3,4,5,6])    # by default it changes to 2d 
# print(arr3.ndim)
# x = arr3.reshape((3,2))   # the reshape() takes two arguements; one is the number of row and other is column
# print(x)
# print(x.ndim)

# reshaping array to higher dimension 
arr4 = np.arange(1,13)
print(arr4)
print(arr4.ndim)
y = arr4.reshape(2,3,2)
print(y)

# in case of changing back the array into 1d 
z = y.reshape(-1)
print(z)
print(z.ndim)