import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr_split = np.split(arr1,2)     # returns the splitted array as a list
print(arr_split)
arr2 = np.array(arr_split)       # returns a two dimension array
print(arr2)

# for two dimension array
arr3 = np.array([[1,2,3,4],[5,6,7,8]])
arr3_split = np.split(arr3, 2)
print(arr3_split)

# the axis attribute can also be used
arr3__split = np.split(arr3, 2, axis=1)
print()
print(arr3__split)
print(arr3__split[0])   # this returns an array
print(arr3__split[1])