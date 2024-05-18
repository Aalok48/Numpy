import numpy as np

# for 1d array
arr1 = np.array([1,2,3,4,5])
# np.insert(array_name, index_value, value)   # insert() takes three attribute... first is the  name of array, second is the index value where the value is to be inserted, third is the value that has to be inserted
print(np.insert(arr1, 2, 45))
# there can be multiple index_value too... the value is inserted to each index value
print(np.insert(arr1, (2,4), 34))

# if float value is taken then only integer part of the float is inserted into the index position
print()

# for two dimension array 
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.insert(arr2, 1, [4,3], axis=1))    # axis means where row or column the data should be inserted
print()
# by using append() function
arr3 = np.append(arr2, [[6,7,8]], axis=0)   # it adds new elements at end of existing array
print(arr3)

# using the delete function
print()
arr1 = np.array([1,2,3,4,5])
print(np.delete(arr1,1))