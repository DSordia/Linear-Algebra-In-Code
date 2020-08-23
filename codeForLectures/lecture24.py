# LECTURE 24 - Markov Matrices; Fourier Series

import numpy as np

# Eigenvalues/eigenvectors of a markov matrix

A = np.array([[.9, .2], [.1, .8]])
evalues, evectors = np.linalg.eig(A)

print(f'Markov matrix A = \n{A}\nEigenvalues of A = {evalues}\nEigenvectors of A = \n{evectors}')

#OUTPUT:
'''
Markov matrix A =
[[0.9 0.2]
 [0.1 0.8]]
Eigenvalues of A = [1.  0.7]
Eigenvectors of A =
[[ 0.89442719 -0.70710678]
 [ 0.4472136   0.70710678]]
'''