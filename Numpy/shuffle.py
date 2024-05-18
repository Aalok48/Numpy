# shuffle
# unique
# resize
# flatten
# ravel

import numpy as np

# np.random.shuffle() function
arr1 = np.array([1,2,3,4,5,6])
np.random.shuffle(arr1)    # shuffles the array in an random way
print(arr1)
print(np.sort(arr1))       # sorts the array
print()

# unique() function
arr2 = np.array([1,2,3,2,3,4,5,4,5,4,6,3,4,5,5,3])
uni = np.unique(arr2, return_index=True, return_counts=True)       # here the unique() returns one element only one time ignoring how many times it is repeated... it more or less similar to the set datatype of python 
print(uni)                                     # the return_index parameter returns the first occuring index of the element in the first array     
# the return_count returns the number of times the element have been repeated
print()

# resize() array
arr3 = np.array([1,2,3,4,5,6])
x = np.resize(arr3, (2,3))    # this function resizes the array according to the parameter passed
print(x)
print()

# flatten() function
# print(x.flatten())         # returns [1 2 3 4 5 6] by default it is 'c' 
# print(x.flatten(order='f'))  # returns [1 4 2 5 3 6]

# ravel() function
print(np.ravel(x))   # ravel function are used to flatten multi-dimensional array into one dimension

# flatten() and ravel() does the same thing i.e changing multi dimension array into 1d array
# but if modifying the flattened array made by using ravel() thenn the modified change is seen into the orginial array whereas the flatten() creates a new copy of the array which can be modified 
