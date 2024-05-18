import numpy as np

# returns int32
# arr1 = np.array([1,2,3,4])
# print("Data type: ", arr1.dtype)

# returns float64
# arr2 = np.array([1.1, 2.2, 3.3])
# print("Data type: ", arr2.dtype)

# returns <u1; means it is of string 
# arr3 = np.array(['a','s','d','f'])
# print("Data type: ", arr3.dtype)

# returns <u11; means mixed data type
# arr4 = np.array(['a','s','d','f',1,2,3,4])
# print("Data type: ", arr4.dtype)

# conversion of one datatype to another in numpy.... By default it is int32
# arr5 = np.array([1,2,3,4,5], dtype=np.int8)   # this converts the int32 datatype into int8 datatype
# print("Data type: ", arr5.dtype)

# data type conversion using astype() function
new = np.array([1,2,3,4])
new_one = new.astype(float)
print(new.dtype)
print(new_one.dtype)