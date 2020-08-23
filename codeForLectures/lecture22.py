# LECTURE 22 - Diagonalization and Powers of A

import numpy as np

# Showing that S inverse * AS = capital lamda

A = np.array([[0, 1], [-2, -3]])
evalues, evectors = np.linalg.eig(A)
S = evectors
Sinv = np.linalg.inv(S)


print(f'Eigenvalues of A = {evalues}\nS inverse * AS = \n{np.dot(np.linalg.inv(S), np.dot(A, S))}')

#OUTPUT:
'''
Eigenvalues of A = [-1. -2.]
S inverse * AS =
[[-1.00000000e+00 -4.36247471e-17]
 [ 6.33024397e-17 -2.00000000e+00]]
''' # eigenvalues across diagonal, rest (basically) 0

# Showing that if Ax = λx, then A^3x = λ^3x, where the eigenvectors are the same

A = np.array([[0, 1], [-2, -3]])
A2 = np.dot(A, np.dot(A, A))
evalues, evectors = np.linalg.eig(A)
evalues2, evectors2 = np.linalg.eig(A2)


print(f'A = \n{A}\nEigenvalues = {evalues}\nEigenvectors = \n{evectors}\nA^3 = \n{A2}\neigenvalues of A^3 = {evalues2}\neigenvectors of A^3 = \n{evectors2}')

#OUTPUT:
'''
A =
[[ 0  1]
 [-2 -3]]
Eigenvalues = [-1. -2.]
Eigenvectors =
[[ 0.70710678 -0.4472136 ]
 [-0.70710678  0.89442719]]
A^3 =
[[  6   7]
 [-14 -15]]
eigenvalues of A^3 = [-1. -8.]
eigenvectors of A^3 =
[[ 0.70710678 -0.4472136 ]
 [-0.70710678  0.89442719]]
'''