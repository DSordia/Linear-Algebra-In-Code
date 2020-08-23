# LECTURE 19 - Determinant Formulas and Cofactors

import numpy as np

# Not too much code for this one.. cofactor expansion is done behind the scenes

# Determinant of a 4x4 matrix

A = np.array([[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 1]])
B = np.array([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]])
print(f'A = \n{A}\nDeterminant of A = {np.linalg.det(A)}')
print(f'B = \n{B}\nDeterminant of B = {np.linalg.det(B)}')

#OUTPUT:
'''
A =
[[0 0 1 1]
 [0 1 1 0]
 [1 1 0 0]
 [1 0 0 1]]
Determinant of A = 0.0
B =
[[1 1 0 0]
 [1 1 1 0]
 [0 1 1 1]
 [0 0 1 1]]
Determinant of B = -1.0
'''