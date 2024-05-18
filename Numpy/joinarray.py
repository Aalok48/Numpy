import numpy as np

# # Jointing one dimensional array
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# arr = np.concatenate((arr1,arr2))
# print(arr)

# Joining two dimensional array
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[0,2,4,6],[1,3,5,7]])
arr_con = np.concatenate((arr1, arr2), axis=1)   # here the axis attribute means defining the direction in which the arrays should be joined... axis 0 is the default and means joining the later array in the bottom of the first array while axis 1 means joining the array column wise... this is the case of two dimensional array and in case of three dimensional array there are three axises
arr_stack = np.stack((arr1, arr2), axis=1)
print(arr_stack)
print(arr_stack.ndim)
print(arr_stack.shape)
# axis 0 means the arrays should be joined vertically whereas axis 1 means arrays should be joined horizontally
# the stack() is also used to join two array
# without using axis the hstack can do same as axis=1 and vstack as axis=0
print()
arr_stack1 = np.vstack((arr1,arr2))
print(arr_stack1)
print()
arr_stack2 = np.hstack((arr1, arr2))
print(arr_stack2)

# the hstack() and vstack() does not alters the dimension of the array whereas the stack() alters
print()
arr_stack3 = np.dstack((arr1, arr2))
print(arr_stack3)