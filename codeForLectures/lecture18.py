# LECTURE 18 - Properties of Determinants

import numpy as np
import math

# Determinant of the 2x2 identity matrix and permutation matrix
I = np.array([[1, 0], [0, 1]])
P = np.array([[0, 1], [1, 0]])
print(f'Determinant of I = {np.linalg.det(I)}\nDeterminant of permutation of I = {np.linalg.det(P)}')

#OUTPUT:
'''
Determinant of I = 1.0
Determinant of permutation of I = -1.0
'''

# Showing that exchanging rows of a matrix reverses the sign of the determinant

A = np.array([[2, -3, 1], [2, 0, -1], [1, 3, 2]])
Flipped = np.array([[1, 3, 2], [2, 0, -1], [2, -3, 1]])

print(f'Determinant of A = {np.linalg.det(A)}\nDeterminant of A with rows 1 and 3 flipped = {np.linalg.det(Flipped)}')

#OUTPUT:
'''
Determinant of A = 27.0
Determinant of A with rows 1 and 3 flipped = -27.0
'''

# Showing that multiplying one row of a matrix by a scalar multiplies the determinant of the whole matrix by that same scalar

A = np.array([[2, -3, 1], [2, 0, -1], [1, 3, 2]])
A2 = np.array([[2, -3, 1], [4, 0, -2], [1, 3, 2]]) #multiplied row 2 by 2

print(f'Determinant of A = {np.linalg.det(A)}\nDeterminant of A after multiplying row 2 by 2 = {round(np.linalg.det(A2))}')

#OUTPUT:
'''
Determinant of A = 27.0
Determinant of A after multiplying row 2 by 2 = 54
'''


# Showing that if any single row of a matrix has values a + a' and b + b', the determinant of the whole matrix is
# the determinant of the matrix with only a and b in the first row plus the determinant of the matrix with only a' and b' in the first row

A = np.array([[2, -3, 1], [1 + 1, 2 + 1, -2 + 1], [1, 3, 2]])
A2 = np.array([[2, -3, 1], [1, 2, -2], [1, 3, 2]])
A3 = np.array([[2, -3, 1], [1, 1, 1], [1, 3, 2]])
print(f'Determinant of A where row 2 is 1 + 1, 2 + 1, -2 + 1: {np.linalg.det(A)}')
print(f'Determinant of A2 with row 2 of 1, 2, -2 plus determinant of A3 with row 2 of 1, 1, 1: {round(np.linalg.det(A2) + np.linalg.det(A3))}')

#OUTPUT:
'''
Determinant of A where row 2 is 1 + 1, 2 + 1, -2 + 1: 36.0
Determinant of A2 with row 2 of 1, 2, -2 plus determinant of A3 with row 2 of 1, 1, 1: 36
'''


# Showing that if any 2 rows in a matrix are equal, the determinant = 0
A = np.array([[2, 3, 4], [1, 2, 3], [1, 2, 3]])
print(f'Determinant of A where rows 2 and 3 are the same: {np.linalg.det(A)}')

#OUTPUT:
'''
Determinant of A where rows 2 and 3 are the same: 0.0
'''

# Showing that det(A+B) is not equal to det A + det B

A = np.array([[2, -3, 1], [2, 0, -1], [1, 3, 2]])
B = np.array([[3, -2, 4], [1, -1, -3], [3, 1, -2]])
AplusB = A + B

print(f'Determinant of A+B = {round(np.linalg.det(AplusB))}, determinant of A + determinant of B = {round(np.linalg.det(A) + np.linalg.det(B))}')

#OUTPUT:
'''
Determinant of A+B = 240, determinant of A + determinant of B = 72
'''


# Showing that subtracting a multiple of one row from another row does not change the determinant

A = np.array([[2, -3, 1], [2, 0, -1], [1, 3, 2]])
A2 = np.array([[2, -3, 1], [-2, 6, -3], [1, 3, 2]]) #row 2 = row 2 - 2*row 1

print(f'Determinant of A = {np.linalg.det(A)}, determinant of A where row 2 = row 2 - 2 * row1 = {np.linalg.det(A2)}')

#OUTPUT:
'''
Determinant of A = 27.0, determinant of A where row 2 = row 2 - 2 * row1 = 27.0
'''

# Showing that if a matrix has a row of zeros, the determinant = 0
A = np.array([[2, -3, 1], [0, 0, 0], [1, 3, 2]])

print(f'Determinant of A where row 2 is all zeros = {np.linalg.det(A)}')

#OUTPUT:
'''
Determinant of A where row 2 is all zeros = 0.0
'''

# The determinant of an upper-triangular matrix

A = np.array([[2, -3, 1], [0, 3, -1], [0, 0, 2]])

print(f'Determinant of upper-triangular A = {np.linalg.det(A)}, the product of the values on the diagonal = {2 * 3 * 2}')

#OUTPUT:
'''
Determinant of upper-triangular A = 12.0, the product of the values on the diagonal = 12
'''

# Showing that the determinant of a matrix A = 0 when A is non-invertible / singular, the determinant ≠ 0 if the matrix is invertible / non-singular

A = np.array([[2, -3, 1], [0, 3, -1], [0, 0, 2]])
B = np.array([[1, 2, 3], [2, 4, 6], [-1, 0, -3]])

print(f'Determinant of A which is invertible = {np.linalg.det(A)}, determinant of B which is non-invertible = {np.linalg.det(B)}')

#OUTPUT:
'''
Determinant of A which is invertible = 12.0, determinant of B which is non-invertible = 0.0
'''

# Showing that det(AB) = det A * det B

A = np.array([[2, -3, 1], [0, 3, -1], [0, 0, 2]])
B = np.array([[3, -2, 1], [-2, 1, 3], [0, 2, -3]])
AB = np.dot(A, B)

print(f'Determinant of A * B = {round(np.linalg.det(AB))}, determinant of A * determinant of B = {round(np.linalg.det(A) * np.linalg.det(B))}')

#OUTPUT:
'''
Determinant of A * B = -228, determinant of A * determinant of B = -228
'''