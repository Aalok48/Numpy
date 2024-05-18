import numpy as np

var1 = np.array([1,2,3,4])
var2 = np.array([[1],[2],[3]])
print(var1+var2)   # this operation works because of broadcasting rules... here var1 is of 1*4 and var2 is of 3*1 so while performing operation between these two array the 1*4 and 3*1 are compared to each other from right side such as 4 from 1*4 and 1 from 3*1 are compared and if anyone of them is one or they are equal then the operation works as normal otherwise it causes an error
print()
print()
print()

arr1 = np.array([[1],[2]])
print(arr1.shape)
arr2 = np.array([[1,2,3],[3,4,5]])
print(arr2.shape)
print(arr1+arr2)
