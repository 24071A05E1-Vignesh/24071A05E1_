#Use NumPy to perform basic matrix operations.
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", A+B)

print("Matrix Subtraction:\n", A-B)

print("Element-wise Multiplication:\n", A*B)

print("Matrix Multiplication (Dot Product):\n", np.dot(A,B))

print("Transpose of A:\n", np.transpose(A))

print("Determinant of A:", np.linalg.det(A))

if np.linalg.det(A) != 0: 
    print("Inverse of A:\n", np.linalg.inv(A))
else:
    print("Matrix A is singular and cannot be inverted.")