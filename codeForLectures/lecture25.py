# LECTURE 25 - Symmetric Matrices and Positive Definiteness

import numpy as np

# Showing that A = AT for a symmetric matrix

A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 8]])

print(f'A = \n{A}\nA Transpose = \n{A.transpose()}')

#OUTPUT:
'''
A =
[[1 2 3]
 [2 4 5]
 [3 5 8]]
A Transpose =
[[1 2 3]
 [2 4 5]
 [3 5 8]]
''' 

# Showing that the eigenvectors of a symmetric matrix are orthogonal

A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 8]])
evalues, evectors = np.linalg.eig(A)

print(f'Eigenvectors of A = \n{evectors}\nDot product of e1 * e2 = {np.dot(evectors[0], evectors[1])},\ne1 * e3 = {np.dot(evectors[0], evectors[2])}\n'
f'e2 * e3 = {np.dot(evectors[1], evectors[2])}')

#OUTPUT:
'''
Eigenvectors of A =
[[ 0.29882628  0.95379458  0.03128512]
 [ 0.53447665 -0.14011391 -0.83348833]
 [ 0.79059317 -0.26578938  0.55165065]]
Dot product of e1 * e2 = -1.1969591984239969e-15,
e1 * e3 = 4.198030811863873e-16
e2 * e3 = 1.6653345369377348e-16
''' # these values are basically 0

# Showing that A = QΛQT

A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 8]])
evalues, evectors = np.linalg.eig(A)

capitalLamda = np.dot(np.linalg.inv(evectors), np.dot(A, evectors))
Q = []
for i in range(0, len(evectors)):
    evectors[i] = evectors[i] / np.linalg.norm(evectors[i])
    Q.append(evectors[i])

capitalLamda = np.array(capitalLamda)
Q = np.array(Q)

print(f'A = \n{A}\nQ * capital lamda * Q tranpose = \n{np.dot(Q, np.dot(capitalLamda, Q.transpose()))}')

#OUTPUT:
'''
A =
[[1 2 3]
 [2 4 5]
 [3 5 8]]
Q * capital lamda * Q tranpose =
[[1. 2. 3.]
 [2. 4. 5.]
 [3. 5. 8.]]
''' 

# Eigenvalues of a positive definite matrix

A = np.array([[5, 2], [2, 3]])
evalues, evectors = np.linalg.eig(A)

print(f'Positive definite matrix A = \n{A}\nDeterminant of A = {np.round(np.linalg.det(A))}\neigenvalues of A = {evalues})'
f'\nproduct of eigenvalues = {round(evalues[0] * evalues[1])}')

#OUTPUT:
'''
Positive definite matrix A =
[[5 2]
 [2 3]]
Determinant of A = 11.0
eigenvalues of A = [6.23606798 1.76393202])
product of eigenvalues = 11
''' #eigenvalues are positive and real as expected