import numpy as np

'''For one dimension array'''

# # addition by an integer
# arr1 = np.array([1,2,3,4])
# arr_add = arr1+3
# print(arr_add)

# addition of an array with another array
# arr2 = np.array([5,6,7,8])
# arr4 = np.array([2,3,4,5])
# arr3 = np.ones(4, dtype=int)  # by default np.ones returns array of float values
# arr_add = arr2 + arr3         # this can also be done by np.add(arr2,arr3)
# arr_sub = arr2 - arr3
# arr_mult = arr2*arr4          # the first element is multiplied by the first element and so on...
# arr_div = arr2/arr4
# arr_modulo = arr2%arr4        # the % returns the remainder 
# arr_power = np.power(arr2, arr4)
# arr5 = np.reciprocal(arr2)    # returns the 1/arr5 array
# print(arr_add)
# print(arr_sub)
# print(arr_mult)
# print(arr_div)
# print(arr_modulo)
# print(arr_power)
# print(arr5)

'''For 2d array'''

# var1 = np.array([[1,2,3,4],[1,2,3,4]])
# var2 = np.array([[1,2,3,4],[1,2,3,4]])
# var_add = np.add(var1, var2)
# var_sub = np.subtract(var1, var2)
# var_mult = np.multiply(var1, var2)
# var_div = np.divide(var1, var2)
# print(var_add)
# print(var_sub)
# print(var_mult)
# print(var_div)       # similarly the modulo, power and ... functions can also be used

'''Some other mathematical functions in numpy'''

# arr1 = np.arange(1,99)
# print(np.max(arr1))    # max() is used for the largest number in the array
# print(np.min(arr1))    # min() is used for the smallest number in the array
# print(np.mean(arr1))   # mean() is used to calculate the average value of all elements in the array
# print(np.median(arr1)) # median() is used to find the middle most value if the list is sorted, else it finds mean
# print(np.argmin(arr1)) # argmin() returns the position of the min element of the array
# print(np.argmax(arr1)) # argmax() returns the position of the max element of the array

'''here when axis is passed, then it returns the max or min element of each row or column according to the axis value... axis 1 is row and axis 0 is column... axis can also be used for other mathematical functions'''
arr1 = np.array([[1,4,8],[24,25,75]]) 
arr2 = np.array([1,2,3,4,5,6])
print(np.min(arr1, axis=0))
print(np.sqrt(arr1))     # the sqrt() returns the square root of the array in float data type
print(np.sin(arr1))      # sin() returns the sin value of the element of the array
print(np.log(arr1))      # log() returns the natural logarithm of the element of the array
print(np.cos(arr1))      # cos() returns the cos value of the element of the array
print(np.cumsum(arr2))   # cumsum() gives the array as the first element is as it is and the second element is the sum of first and second... the third is the sum of first,second and third and so on