# LECTURE 10 - The Four Fundamental Subspaces

import numpy as np
from sympy import *

# The four fundamental subspaces of a matrix

A = Matrix([[1, 2, 3, 1], [1, 1, 2, 1], [1, 2, 3, 1]])

print(f'A = \n{A}\nColumn space of A = \n{A.columnspace()}\nNull space of A = \n{A.nullspace()}\nRow space of A = \n{A.T.columnspace()}\nLeft null space = \n{A.T.nullspace()}')

#OUTPUT:
'''
Column space of A = 
[Matrix([
[1],
[1],
[1]]), Matrix([
[2],
[1],
[2]])]
Null space of A = 
[Matrix([
[-1],
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 0],
[ 1]])]
Row space of A =
[Matrix([
[1],
[2],
[3],
[1]]), Matrix([
[1],
[1],
[2],
[1]])]
Left null space =
[Matrix([
[-1],
[ 0],
[ 1]])]
'''