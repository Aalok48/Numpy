import numpy as np

# creating a zero array
array_zero = np.zeros(4)  # this creates a single dimension array
array_zero1 = np.zeros((3,4))  # this creates a 2-d array 

# this means this is a three dimension array having four matrix like array of rows three and column four
array_zero2 = np.ones((4,3,4))  
#print(array_zero)
#print()   # this prints a blank statement
#print(array_zero1)
#print()
print(array_zero2)
print()

# creating an empty array
arr_empty = np.empty(4)
print(arr_empty)

# creating an array having elements in a range
arr_range = np.arange(2,8)   # this returns elements same as a loop
print(arr_range)

# creating an array whose diagonal elements are filled with 1's 
arr_diagonal = np.eye(5)  # this creates a 2d array having diagonal elements 1
print(arr_diagonal)
print()
# for custom array
arr_diagona2 = np.eye(3,5)
print(arr_diagona2)
print()

# creating an array in a certain pattern in a certain interval
arr_linspace = np.linspace(0,20,num=5) # this means start from 0 and end in 20 with total number of array elements to be 5
print(arr_linspace)