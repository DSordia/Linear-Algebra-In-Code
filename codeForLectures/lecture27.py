# LECTURE 27 - Positive Definite Matrices and Minima

import numpy as np

# Determinant and eigenvalues of a non-positive-definite matrix,
# a semi-positive-definite matrix, and a positive-definite matrix

A = np.array([[2, 6], [6, 7]])
B = np.array([[2, 6], [6, 18]])
C = np.array([[2, 6], [6, 20]])

print(f'Non-positive-definite matrix = \n{A}\nDeterminant = {np.linalg.det(A)}\nEigenvalues = {np.linalg.eig(A)[0]}\n'
f'Semi-positive-definite matrix = \n{B}\nDeterminant = {np.linalg.det(B)}\nEigenvalues = {np.linalg.eig(B)[0]}\n'
f'Positive-definite matrix = \n{C}\nDeterminant = {np.linalg.det(C)}\nEigenvalues = {np.linalg.eig(C)[0]}')

#OUTPUT:
'''
Non-positive-definite matrix = 
[[2 6]
 [6 7]]
Determinant = -22.000000000000004
Eigenvalues = [-2. 11.]
Semi-positive-definite matrix = 
[[ 2  6]
 [ 6 18]]
Determinant = 0.0
Eigenvalues = [ 0. 20.]
Positive-definite matrix =
[[ 2  6]
 [ 6 20]]
Determinant = 3.9999999999999964
'''# first has negative determinant and eigenvalue, second has 0 determinant and eigenvalue, third has positive determinant and eigenvalue as expected