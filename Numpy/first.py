import numpy as np

# creating an array x
#x = np.array([1,2,3,4])
#print(x)

# creating an array y
#y = np.arange(1,9)**46
#print(y)

# creating an array l1
#l1 = [5,6,7,8]
#print(np.array(l1))

# l1=[]
# n=1
# while n<=5:
# x = int(input("Enter a number:"))
# l1.append(x)
# n+=1
# print(np.array(l1))

# checking the dimension of the array
# x = np.array([1,2,3,4,5])     # single square bracket means 1-dim array
# y = np.array([[11,21,31,41,51]]) # double square bracket means 2-dim
# print(x.ndim, y.ndim)

# creating a 2-dimensional array

# arr1 = [[1,2,3,4],[5,6,7,8]] # here two list are passed in arr1, so for the array the number of items for both the list must be same and they should be of same data type
# arr2 = np.array(arr1)
# print(arr2)
# print(arr2.ndim)

# creating a 3-dimensional array

# arr1 = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]
# arr2 = np.array(arr1)
# print(arr2)
# print(arr2.ndim)

# creating a higher dimension array such as a ten dimension

arn = np.array([1,2,3,4], ndmin=10)
print(arn)
print(arn.ndim)