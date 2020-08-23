# LECTURE 28 - Similar Matrices and Jordan Form

import numpy as np

# Showing that if a matrix is positive-definite, its inverse is positive-definite

A = np.array([[2, 6], [6, 20]])
Ainv = np.linalg.inv(A)
evalues, evectors = np.linalg.eig(Ainv)

print(f'Positive definite matrix A = \n{A}\nEigenvalues of A inverse = {evalues}\nDeterminant of A inverse = {np.linalg.det(Ainv)}')

#OUTPUT:
'''
Positive definite matrix A = 
[[ 2  6]
 [ 6 20]]
Eigenvalues of A inverse = [5.45416346 0.04583654]
Determinant of A inverse = 0.25000000000000044
''' #eigenvalues and determinant > 0

# Showing that if two matrices A and B are positive-definite, A + B is positive definite

A = np.array([[2, 6], [6, 20]])
B = np.array([[7, 2], [2, 1]])
AplusB = A + B
evalues, evectors = np.linalg.eig(AplusB)

print(f'Positive definite matrices A and B = \n{A}\n{B}\nEigenvalues of A + B = {evalues}\nDeterminant of A + B = {np.linalg.det(AplusB)}')

#OUTPUT:
'''
Positive definite matrices A and B = 
[[ 2  6]
 [ 6 20]]
[[7 2]
 [2 1]]
Eigenvalues of A + B = [ 5. 25.]
Determinant of A + B = 125.00000000000004
''' #eigenvalues and determinant > 0

# Showing that A transpose * A is positive-definite if A is invertible

A = np.array([[1, 2, 3], [-2, 4, 1], [-3, 0, 2]])
ATA = np.dot(A.transpose(), A)
evalues, evectors = np.linalg.eig(ATA)

print(f'A = \n{A}\nEigenvalues of ATA = {evalues}\nDeterminant of ATA = {np.linalg.det(ATA)}')

#OUTPUT:
'''
A =
[[ 1  2  3]
 [-2  4  1]
 [-3  0  2]]
Eigenvalues of ATA = [31.01591355 10.46479645  6.51929   ]
Determinant of ATA = 2115.9999999999986
'''

# Showing that two matrices A and B are similar

A = np.array([[2, 1], [1, 2]])
evaluesA, evectorsA = np.linalg.eig(A)

B = np.array([[3, 0], [0, 1]])
evaluesB, evectorsB = np.linalg.eig(B)

print(f'Eigenvalues of A = {evaluesA}\nNumber of eigenvectors of A = {len(evectorsA)}\nEigenvalues of B = {evaluesB}\nNumber of eigenvectors of B = {len(evectorsB)}')

#OUTPUT:
'''
Eigenvalues of A = [3. 1.]
Number of eigenvectors of A = 2
Eigenvalues of B = [3. 1.]
Number of eigenvectors of B = 2
'''