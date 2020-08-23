# LECTURE 8 - Solving Ax = b: Row Reduced Form R

import numpy as np
from sympy import *

# A = Matrix([[1, 2, 2, 2, -1], [2, 4, 6, 8, -5], [3, 6, 8, 10, -6]])
# print(f'A = \n{A}\nColumn space of A = \n{A.columnspace()}')

A = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
b = np.array([[1], [5], [6]])
print(f'A = \n{A}\nb = \n{b}\nx = \n{np.linalg.lstsq(A, b)}')
print(f'This is correct..\n1*-0.13793103 + 2*-0.27586207 + 2*0.18965517 + 2*0.65517241 = {round(1*-0.13793103 + 2*-0.27586207 + 2*0.18965517 + 2*0.65517241, 2)}'
f'\n2*-0.13793103 + 4*-0.27586207 + 6*0.18965517 + 8*0.65517241 = {round(2*-0.13793103 + 4*-0.27586207 + 6*0.18965517 + 8*0.65517241, 2)}'
f'\n3*-0.13793103 + 6*-0.27586207 + 8*0.18965517 + 10*0.65517241 = {round(3*-0.13793103 + 6*-0.27586207 + 8*0.18965517 + 10*0.65517241, 2)}')

#OUTPUT:
'''
A =
[[ 1  2  2  2]
 [ 2  4  6  8]
 [ 3  6  8 10]]
b =
[[1]
 [5]
 [6]]
x =
(array([[-0.13793103],
       [-0.27586207],
       [ 0.18965517],
       [ 0.65517241]]), array([], dtype=float64), 2, array([1.84656278e+01, 1.01024229e+00, 5.73316705e-16]))
This is correct..
1*-0.13793103 + 2*-0.27586207 + 2*0.18965517 + 2*0.65517241 = 1.0
2*-0.13793103 + 4*-0.27586207 + 6*0.18965517 + 8*0.65517241 = 5.0
3*-0.13793103 + 6*-0.27586207 + 8*0.18965517 + 10*0.65517241 = 6.0
'''

# Rank of a 4x2 and 2x4 matrix

A = np.array([[1, 3], [2, 1], [6, 1], [5, 1]])
B = A.transpose()

print(f'A = \n{A}\nB = \n{B}\nRank of A = {np.linalg.matrix_rank(A)}\nRank of B = {np.linalg.matrix_rank(B)}')

#OUTPUT:
'''
A =
[[1 3]
 [2 1]
 [6 1]
 [5 1]]
B =
[[1 2 6 5]
 [3 1 1 1]]
Rank of A = 2
Rank of B = 2
'''

# rref of a 4x2 and 2x4 matrix

A = Matrix([[1, 3], [2, 1], [6, 1], [5, 1]])
B = A.T
print(f'A = \n{A}\nB = \n{B}\nrref of A = \n{A.rref()}\nrref of B = \n{B.rref()}')

#OUTPUT:
'''
A =
Matrix([[1, 3], [2, 1], [6, 1], [5, 1]])
B =
Matrix([[1, 2, 6, 5], [3, 1, 1, 1]])
rref of A =
(Matrix([
[1, 0],
[0, 1],
[0, 0],
[0, 0]]), (0, 1))
rref of B =
(Matrix([
[1, 0, -4/5, -3/5],
[0, 1, 17/5, 14/5]]), (0, 1))
'''

# rref of an invertible matrix

A = Matrix([[1, 2], [3, 1]])

print(f'A = \n{A}\nrref(A) = \n{A.rref()}')

#OUTPUT:
'''
A =
Matrix([[1, 2], [3, 1]])
rref(A) =
(Matrix([
[1, 0],
[0, 1]]), (0, 1))
'''

# Nullspace of an invertible matrix

print(f'A = \n{A}\nNullspace of A = \n{A.nullspace()}')

#OUTPUT:
'''
A =
Matrix([[1, 2], [3, 1]])
Nullspace of A =
[]
'''