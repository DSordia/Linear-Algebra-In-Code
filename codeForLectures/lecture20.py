# LECTURE 20 - Cramer's Rule, Inverse Matrix, and Volume

import numpy as np
import math

# Cramer's Rule

#Ax = b
A = np.array([[1, 2, 3], [-2, 1, -3], [0, 2, -1]])
b = np.array([[2], [4], [-1]])

print(f'x from solving Ax = b with elimination = \n{np.round(np.linalg.solve(A, b), 2)}')

#Now applying Cramer's rule

x2 = []
#replace each column with b
B1 = np.array([[2, 2, 3], [4, 1, -3], [-1, 2, -1]])
B2 = np.array([[1, 2, 3], [-2, 4, -3], [0, -1, -1]])
B3 = np.array([[1, 2, 2], [-2, 1, 4], [0, 2, -1]])

x2.append(round(np.linalg.det(B1) / np.linalg.det(A), 2))
x2.append(round(np.linalg.det(B2) / np.linalg.det(A), 2))
x2.append(round(np.linalg.det(B3) / np.linalg.det(A), 2))

print(f'x using Cramer\'s rule = \n{x2}')

#OUTPUT:
'''
x from solving Ax = b with elimination =
[[-4.64]
 [ 0.45]
 [ 1.91]]
x using Cramer's rule =
[-4.64, 0.45, 1.91]
'''

# Showing that |det A| = volume of a box

print(f'take a box with length 3, width 2, height 4 - the volume is 3 * 2 * 4 = {3 * 2 * 4}')

A = np.array([[3, 0, 0], [0, 2, 0], [0, 0, 4]])

print(f'determinant of a matrix A representing this box = {round(np.linalg.det(A))}')

#OUTPUT:
'''
take a box with length 3, width 2, height 4 - the volume is 3 * 2 * 4 = 24
determinant of a matrix A representing this box = 24
'''