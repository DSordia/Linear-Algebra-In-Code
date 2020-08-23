# LECTURE 7 - Solving Ax = 0: Pivot Variables, Special Solutions

import numpy as np
from sympy import *

# Solving Ax = 0 for 3x4 matrix - two lines with SymPy!

A = Matrix([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
print(f'A = \n{A}\nNullspace of A = \n{A.nullspace()}')

#OUTPUT:
'''
A =
Matrix([[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]])
Nullspace of A =
[Matrix([
[-2],
[ 1],
[ 0],
[ 0]]), Matrix([
[ 2],
[ 0],
[-2],
[ 1]])]
'''

# Rank of a Matrix

A = np.array([[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]])
print(f'A = \n{A}\nRank of A = {np.linalg.matrix_rank(A)}')

#OUTPUT:
'''
A =
[[1 2 2 2]
 [0 0 2 4]
 [0 0 0 0]]
Rank of A = 2
'''

# rref(A)

A = Matrix([[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]])
print(f'A = \n{A}\nrref of A = \n{A.rref()}')

#OUTPUT:
'''
A =
Matrix([[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]])
rref of A =
(Matrix([
[1, 2, 0, -2],
[0, 0, 1,  2],
[0, 0, 0,  0]]), (0, 2))
'''