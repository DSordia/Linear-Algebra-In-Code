# LECTURE 14 - Orthogonal Vectors and Subspaces

import numpy as np
from sympy import *

# See if two vectors are orthogonal

x = np.array([1, 2, 3])
y = np.array([2, -1, 0])

print(f'The dot product of x and y is {np.dot(x, y)}, so x and y are orthogonal')

#OUTPUT:
'''
The dot product of x and y is 0, so x and y are orthogonal
'''

# Show that the row space is orthogonal to the null space

A = Matrix([[1, 2, 5], [2, 4, 10]])
Arowspace = A.T.columnspace()
Anullspace = A.nullspace()

print(f'A = \n{A}\nRow space of A = \n{Arowspace}\nNull space of A = \n{Anullspace}')

Arowspace = np.array(Arowspace).astype(np.float64)
Anullspace = np.array(Anullspace).astype(np.float64)

print(f'Dot product of the row space with the first vector in the null space = \n{np.concatenate(np.concatenate(Arowspace)).dot(np.concatenate(Anullspace[0]))}')
print(f'Dot product of the row space with the second vector in the null space = \n{np.concatenate(np.concatenate(Arowspace)).dot(np.concatenate(Anullspace[1]))}')

#OUTPUT:
'''
A =
Matrix([[1, 2, 5], [2, 4, 10]])
Row space of A =
[Matrix([
[1],
[2],
[5]])]
Null space of A =
[Matrix([
[-2],
[ 1],
[ 0]]), Matrix([
[-5],
[ 0],
[ 1]])]
Dot product of the row space with the first vector in the null space =
0.0
Dot product of the row space with the second vector in the null space =
0.0
'''

# Show that the column space is orthogonal to the left null space

A = Matrix([[1, 2, 5], [2, 4, 10]])
Acolspace = A.columnspace()
Aleftnullspace = A.T.nullspace()

print(f'A = \n{A}\nColumn space of A = \n{Acolspace}\nLeft null space of A = \n{Aleftnullspace}')

Acolspace = np.array(Acolspace).astype(np.float64)
Aleftnullspace = np.array(Aleftnullspace).astype(np.float64)

print(f'Dot product of the column space with the vector in the left null space = \n{np.concatenate(np.concatenate(Acolspace)).dot(np.concatenate(Aleftnullspace))}')

#OUTPUT:
'''
A =
Matrix([[1, 2, 5], [2, 4, 10]])
Column space of A =
[Matrix([
[1],
[2]])]
Left null space of A =
[Matrix([
[-2],
[ 1]])]
Dot product of the column space with the vector in the left null space =
[0.]
'''

# Show that the null space and rank of A transpose * A = null space and rank of A

A = Matrix([[1, 1], [1, 2], [1, 5]])

print(f'A = \n{A}\nRank of A = {A.rank()}\nNull space of A = \n{A.nullspace()}\nRank of A transpose * A = {(A.T * A).rank()}\nNull space of A transpose * A = \n{(A.T * A).nullspace()}')

#OUTPUT:
'''
A =
Matrix([[1, 1], [1, 2], [1, 5]])
Rank of A = 2
Null space of A =
[]
Rank of A transpose * A = 2
Null space of A transpose * A =
[]
'''