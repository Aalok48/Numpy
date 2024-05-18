import numpy as np

var1 = np.matrix([[1,2,3],[2,3,4]])
var2 = np.matrix([[1,2,3],[2,3,4]])
print(var1)
print(type(var1))      # although the array and matrix looks like same they can be differentiated using the type method
print()
print(var1+var2)
print()
# in matrix multiplication is like row is  multiplied by column
arr1 = np.matrix([[1,2,3],[2,3,4]])
arr2 = np.array([[3,5], [7,8],[3,4]]) # array not a matrix
print(arr1*arr2)