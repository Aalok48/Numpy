import numpy as np

# copy() function
arr1 = np.array([1,2,3,4,5])
copy_arr = arr1.copy()
print(copy_arr)

# view() function
arr2 = arr1.view()
print(arr2)