import numpy as np

# transpose of the matrix
mat1 = np.matrix([[1,2,3],[4,5,6]])
print(np.matrix.transpose(mat1))
print(mat1.T)      # this method also returns the transpose of the matrix
print()

# swapaxes of the matrix
print(np.matrix.swapaxes(mat1,0,1))   # the 0,1 means changing the axis 0 into axis 1

# the swapaxes may seem similar to 2by2 matrix but the difference is clearly seem to matrices other than 2by2
print()
# Inverse matrix
mat2 = np.matrix([[1,2], [3,4]])
print(np.linalg.inv(mat2))     # np.linalg.inv(matrix) is used to find out the inverse of the matrix

# Power of matrix
print(np.power(mat2,2))
print()
# other method
print(np.linalg.matrix_power(mat2, n=2))   # n = 2 means the matrix is itself multiplied by 2 times... n = 0 returns identity matrix
print()
print(mat2)
print()
# determinant of the matrix
print(int(np.linalg.det(mat2)))      # the np.linalg.det(matrix) returns the determinant of the matrix
