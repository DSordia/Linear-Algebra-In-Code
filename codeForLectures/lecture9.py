# LECTURE 9 - Independence, Basis, and Dimension

import numpy as np
from sympy import *

# Ax = 0 for an m x n matrix with m < n

A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f'A = \n{A}\nnullspace of A = \n{A.nullspace()}\n')

#OUTPUT:
'''
A = 
Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
nullspace of A =
[Matrix([
[ 1],
[-2],
[ 1],
[ 0]]), Matrix([
[ 2],
[-3],
[ 0],
[ 1]])]
'''

# Check if vectors form a basis by checking the null space

A = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f'A = \n{A}\nnullspace of A = \n{A.nullspace()}\nSo these columns form a basis')

#OUTPUT:
'''
A =
Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
nullspace of A =
[]
So these columns form a basis
'''

A = Matrix([[1, 2], [1, 2], [2, 5]])

print(f'A = \n{A}\nnullspace of A = \n{A.nullspace()}\nSo these columns form a basis')

#OUTPUT:
'''
A =
Matrix([[1, 2], [1, 2], [2, 5]])
nullspace of A =
[]
So these columns form a basis
'''

A = Matrix([[1, 2, 3, 1], [1, 1, 2, 1], [1, 2, 3, 1]])

print(f'A = \n{A}\nnullspace of A = \n{A.nullspace()}\nSo these columns do not form a basis')

A = Matrix([[1, 2], [1, 1], [1, 2]])

print('However, taking only the first 2 columns which are linearly independent gives:')
print(f'A = \n{A}\nnullspace of A = \n{A.nullspace()}\nSo these columns do form a basis')

#OUTPUT:
'''
A =
Matrix([[1, 2, 3, 1], [1, 1, 2, 1], [1, 2, 3, 1]])
nullspace of A =
[Matrix([
[-1],
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 0],
[ 1]])]
So these columns do not form a basis
However, taking only the first 2 columns which are linearly independent gives:
A =
Matrix([[1, 2], [1, 1], [1, 2]])
nullspace of A =
[]
So these columns do form a basis
'''