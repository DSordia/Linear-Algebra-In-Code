# LECTURE 17 - Orthogonal Matrices and Gram-Schmidt

import numpy as np

# Showing that Q tranpose =  inverse and Q transpose * Q = I where Q is a 3x3 permutation matrix

Q = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

print(f'Q = \n{Q}\nQ transpose = \n{Q.transpose()}\nQ inverse = \n{np.linalg.inv(Q)}\nQ tranpose * Q = \n{np.inner(Q.transpose(), np.linalg.inv(Q))}')

#OUTPUT:
'''
Q =
[[0 0 1]
 [1 0 0]
 [0 1 0]]
Q transpose =
[[0 1 0]
 [0 0 1]
 [1 0 0]]
Q inverse =
[[0. 1. 0.]
 [0. 0. 1.]
 [1. 0. 0.]]
Q tranpose * Q =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

# Gram-Schmidt process for 2 vectors

a = np.array([1, 1, 1], dtype = float)
b = np.array([1, 0, 2])

A = a
B = b - ((np.dot(A.transpose(), b) / (np.dot(A.transpose(), A)) * A))

print(f'B = \n{B}')
print(f'Check that A and B are orthogonal: A dot B = {np.dot(A, B)}')

magnitudeA = np.linalg.norm(A)
magnitudeB = np.linalg.norm(B)

for i in range(0, len(A)):
    A[i] = round(A[i] / magnitudeA, 3)
    B[i] = round(B[i] / magnitudeB, 3)

print(f'a and b as unit vectors q1 and q2 (which make up the orthonormal basis): \n{A}\n{B}')

#OUTPUT:
'''
B =
[ 0. -1.  1.]
Check that A and B are orthogonal: A dot B = 0.0
a and b as unit vectors q1 and q2 (which make up the orthonormal basis):
[0.577 0.577 0.577]
[ 0.    -0.707  0.707]
'''



