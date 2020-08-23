# LECTURE 30 - Linear Transformations and Their Matrices

import numpy as np

# Example of a linear transformation T(v) = Av

v = np.array([1, 2])
A = np.array([[1, 0], [0, -1]])

print(f'v = \n{v}\nA = \n{A}\nAv = \n{np.dot(A, v)}')

#OUTPUT:
'''
v =
[1 2]
A =
[[ 1  0]
 [ 0 -1]]
Av =
[ 1 -2]
''' #In this case, T flips the sign of the y component of the vector, which implies T is a reflection across the x axis of the xy-plane