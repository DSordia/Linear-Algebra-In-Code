# LECTURE 21 - Eigenvalues and Eigenvectors

import numpy as np

# Eigenvalues/eigenvectors of a projection matrix

A = np.array([[0, 1], [0, 1]])
evalues, evectors = np.linalg.eig(A)

print(f'A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}')

#OUTPUT:
'''
A =
[[0 1]
 [0 1]]
Eigenvalues of A = [0. 1.]
Eigenvectors of A =
[[1.         0.70710678]
 [0.         0.70710678]]
'''

# Eigenvalues/eigenvectors of a permutation matrix

A = np.array([[0, 1], [1, 0]])
evalues, evectors = np.linalg.eig(A)

print(f'A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}')

#OUTPUT:
'''
A =
[[0 1]
 [1 0]]
Eigenvalues of A = [ 1. -1.]
Eigenvectors of A =
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
'''

# Eigenvalues/eigenvectors of a symmetric matrix

A = np.array([[3, 1], [1, 3]])
evalues, evectors = np.linalg.eig(A)

print(f'A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}')

#OUTPUT:
'''
A =
[[3 1]
 [1 3]]
Eigenvalues of A = [4. 2.]
Eigenvectors of A =
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
'''

# Eigenvalues/eigenvectors of a matrix A and A + 3I

A = np.array([[3, 1], [1, 3]])
B = np.array([[3 + 3, 1], [1, 3 + 3]]) #adding 3 to the values on the diagonal
evalues, evectors = np.linalg.eig(A)
evalues2, evectors2 = np.linalg.eig(B)

print(f'A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}\nEigevalues of A + 3I = {evalues2}\nEigenvectors of A + 3I = \n{evectors2}')

#OUTPUT:
'''
A =
[[3 1]
 [1 3]]
Eigenvalues of A = [4. 2.]
Eigenvectors of A =
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
Eigevalues of A + 3I = [7. 5.]
Eigenvectors of A + 3I =
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
'''


# Showing that the eigenvalues of a matrix A plus or times the eigenvalues of a matrix B are not necessarily the eigenvalues of A+B or A*B

A = np.array([[3, 1], [1, 3]])
B = np.array([[1, 2], [-1, 4]])
AplusB = A + B
AtimesB = A * B
evalues, evectors = np.linalg.eig(A)
evalues2, evectors2 = np.linalg.eig(B)
evalues3, evectors3 = np.linalg.eig(AplusB)
evalues4, evectors4 = np.linalg.eig(AtimesB)

print(f'Eigenvalues of A = {evalues}\nEigenvalues of B = {evalues2}\nEigenvalues of A+B = {evalues3}\nEigenvalues of A + Eigenvalues of B = {evalues + evalues2}\n'
f'Eigenvalues of A*B = {evalues4}\nEigenvalues of A * Eigenvalues of B = {evalues * evalues2}')

#OUTPUT:
'''
Eigenvalues of A = [4. 2.]
Eigenvalues of B = [2. 3.]
Eigenvalues of A+B = [4. 7.]
Eigenvalues of A + Eigenvalues of B = [6. 5.]
Eigenvalues of A*B = [ 3.22799813 11.77200187]
Eigenvalues of A * Eigenvalues of B = [8. 6.]
'''

# Eigenvalues/eigenvectors of an orthogonal matrix Q

Q = np.array([[0, -1], [1, 0]])
evalues, evectors = np.linalg.eig(Q)

print(f'Q = \n{Q}\nEigenvalues of Q = {evalues}\nEigenvectors of Q = \n{evectors}')

#OUTPUT:
'''
Q =
[[ 0 -1]
 [ 1  0]]
Eigenvalues of Q = [0.+1.j 0.-1.j]
Eigenvectors of Q =
[[0.70710678+0.j         0.70710678-0.j        ]
 [0.        -0.70710678j 0.        +0.70710678j]]
''' #complex roots

# Eigenvalues/eigenvectors of a triangular matrix

A = np.array([[3, 1], [0, 3]])
evalues, evectors = np.linalg.eig(A)

print(f'A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}')

#OUTPUT:
'''
Eigenvalues of A = [3. 3.]
Eigenvectors of A =
[[ 1.00000000e+00 -1.00000000e+00]
 [ 0.00000000e+00  6.66133815e-16]]
''' #eigenvalues are the diagonal values. First eigenvector is correct; [1, 0], second is garbage due to repeated eigenvalue
