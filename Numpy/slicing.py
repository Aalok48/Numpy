import numpy as np

# Slicing for 2d array
arr1 = np.arange(0,10)
print(arr1[1:6])    # slicing works as it starts from index 1 and stops one index ahead same as that of list
print(arr1[1:6:3])  # the third attribute is the step meaning that much index is skipped 
print(arr1[::-1])   # this reverses the array :)
print()

# Slicing for 2d array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1,1:5])  # the two dimension array is indexed first then sliced... the first attribute takes the row then then the slicing is done as done earlier
