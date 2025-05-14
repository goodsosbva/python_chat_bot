import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[1, 3, 3], [4, 7, 6]])
print(matrix1 + matrix2)

a = np.array([ [1, 2], [3, 4], [5, 6] ])
b = np.array([ [2, 3], [2, 3] ])
c = np.matmul(a, b)
print(c)

q = np.array([ [2, 3], [2, 3] ])
k = 10
c = k * q
print(c)