# LECTURE 33 - Left and Right Inverses; Pseudoinverse

import numpy as np
from sympy import *

# Left inverse of a matrix

A = Matrix([[1, 3], [2, 1], [6, 1], [5, 1]])
LeftInverse = ((A.T * A)**-1) * A.T

print(f'A = \n{A}\nDimensions of A = \n{A.shape}\nRank of A = \n{A.rank()}\nNull space of A = \n{A.nullspace()}'
f'\nLeft inverse of A = (ATA)^-1*AT = \n{LeftInverse}\nLeft inverse * A = \n{LeftInverse * A}')

#OUTPUT:
'''
A =
Matrix([[1, 3], [2, 1], [6, 1], [5, 1]])
Dimensions of A =
(4, 2)
Rank of A =
2
Null space of A =
[]
Left inverse of A = (ATA)^-1*AT =
Matrix([[-9/134, 1/67, 7/67, 11/134], [91/268, 17/268, -15/268, -7/268]])
Left inverse * A =
Matrix([[1, 0], [0, 1]])
'''

# Right inverse of a matrix

A = Matrix([[1, 2, 6, 5], [3, 1, 1, 1]])
RightInverse = A.T * ((A * A.T))**-1

print(f'A = \n{A}\nDimensions of A = \n{A.shape}\nRank of A = \n{A.rank()}\nLeft Null space of A = \n{A.T.nullspace()}'
f'\nRight inverse of A = AT(AAT)^-1 = \n{RightInverse}\nA * Right inverse = \n{A * RightInverse}')

#OUTPUT:
'''
A =
Matrix([[1, 2, 6, 5], [3, 1, 1, 1]])
Dimensions of A =
(2, 4)
Rank of A =
2
Left Null space of A =
[]
Right inverse of A = AT(AAT)^-1 =
Matrix([[-9/134, 91/268], [1/67, 17/268], [7/67, -15/268], [11/134, -7/268]])
A * Right inverse =
Matrix([[1, 0], [0, 1]])
'''

#Pseudoinverse of a matrix

A = np.array([[1, 3], [5, 7], [11, 13]])

PseudoInverse = np.linalg.pinv(A)

print(f'A = \n{A}\nPseudoinverse of A = \n{PseudoInverse}\nA+ * A = \n{np.dot(PseudoInverse, A)}')

#OUTPUT:
'''
A =
[[ 1  3]
 [ 5  7]
 [11 13]]
Pseudoinverse of A =
[[-0.51973684 -0.21710526  0.23684211]
 [ 0.42763158  0.20394737 -0.13157895]]
A+ * A =
[[1.00000000e+00 1.02695630e-15]
 [1.91513472e-15 1.00000000e+00]]
''' # note A+ * A is the identity matrix