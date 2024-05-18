import numpy as np

# search method returns the index of the element searched
arr1 = np.array([1,2,3,4,5,2,3,4,6,8])
x = np.where(arr1==2)    # returns the index of 2.. if 2 is multiple times in the array then it returns the list of the index values and it also returns the dtype\
print(x)
print()
# some condition can also be passed to the attribute of where
y = np.where(arr1%2==0)   # this checks which element when divided by 2 has remainder 0 and then returns the index of those element as list
print(y)
print()

# searchsorted array
arr2 = np.sort(arr1)      # sorting the arr1 and storing it in arr2
x = np.searchsorted(arr2, 7)   # searchsorted() returns the index in the sorted array where the element'7 in this case' can be included
# y = np.searchsorted(arr2, 7, side='right')
y = np.searchsorted(arr2, [3,8,7])
print(arr2)
print(x)
print(y)
print()

# Sorting 2d array
arr3 = np.array([[30,3,7],[534,123,32],[5,4,3]])   # the array rows are sorted then the array is printed
print(np.sort(arr3))