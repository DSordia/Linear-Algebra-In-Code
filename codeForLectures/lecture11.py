# LECTURE 11 - Matrix Spaces; Rank 1; Small World Graphs

import numpy as np
from sympy import *

# Standard basis for M (all 3x3 matrices) - taken from https://stackoverflow.com/a/44969041/12733759
d, e = 3, 3
basis = np.eye(d*e,d*e).reshape((d*e,d,e))
print(basis)

#OUTPUT:
'''
[[[1. 0. 0.] 
  [0. 0. 0.] 
  [0. 0. 0.]]

 [[0. 1. 0.] 
  [0. 0. 0.] 
  [0. 0. 0.]]

 [[0. 0. 1.]
  [0. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [1. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 1. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 1.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [1. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 1. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 1.]]]
'''

# Column space, row space, and their dimensions for a 2x3 matrix

A = Matrix([[1, 4, 5], [2, 8, 10]])
Colspace = A.columnspace()
Rowspace = A.T.columnspace()

print(f'A = \n{A}\nRank of A = {A.rank()}\nColumn space of A = \n{Colspace}\nDimension of column space = {len(np.array(Colspace).astype(np.float64))}\nRow space of A = \n{Rowspace}\nDimension of row space = {len(np.array(Rowspace).astype(np.float64))}')

#OUTPUT:
'''
A =
Matrix([[1, 4, 5], [2, 8, 10]])
Rank of A = 1
Column space of A =
[Matrix([
[1],
[2]])]
Dimension of column space = 1
Row space of A =
[Matrix([
[1],
[4],
[5]])]
Dimension of row space = 1
'''