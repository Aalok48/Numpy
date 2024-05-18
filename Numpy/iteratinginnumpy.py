import numpy as np

# Iteration in 1d array
arr1 = np.arange(0,10)
for i in arr1:
    print(i)

print()

# Iteration in 2d array
arr2 = np.array([[1,2,3,4],[6,7,8,9]])
for i in arr2:
    for j in i:
        print(j)
print()

# Iteration in 3d array
arr3 = np.array([[[1,2,3,4],[3,4,5,6]]])    # for n dimension we have to use n number of loops
print(arr3.ndim)
print(arr3.shape)     
# for i in arr3:
#     for j in i:       # this is by using for loop; we can also use np.nditer() function which gives the same output
#         for k in j:
#             print(k) 

for i in np.nditer(arr3, flags=['buffered'],op_dtypes=['S']):   # here other parameters are also passed which changes the output to string datatype
    print(i)

print()
# if you want to print index while using loop then
for i,d in np.ndenumerate(arr3):
    print(i,d)       # here i gives the index of element of the array; 
