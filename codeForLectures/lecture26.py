# LECTURE 26 - Complex Matrices; Fast Fourier Transform

import numpy as np

# Magnitude of a complex vector

complexvect = np.matrix([[1], [1j]])

print(f'Complex vector = \n{complexvect}\nMagnitude of vector = {np.dot(complexvect.getH(), complexvect)}')

#OUTPUT:
'''
Complex vector =
[[1.+0.j]
 [0.+1.j]]
Magnitude of vector = [[2.+0.j]]
'''

# Showing that AH = A for a hermitian matrix

C = np.matrix([[2, 3 + 1j], [3 - 1j, 5]])

print(f'Complex matrix C = \n{C}\nC hermitian = \n{C.getH()}')

#OUTPUT:
'''
Complex matrix C =
[[2.+0.j 3.+1.j]
 [3.-1.j 5.+0.j]]
C hermitian =
[[2.-0.j 3.+1.j]
 [3.-1.j 5.-0.j]]
'''

# Showing that QHQ = I for a hermitian matrix

C = np.matrix([[2, 3 + 1j], [3 - 1j, 5]])

evalues, evectors = np.linalg.eig(C)

print(f'Q = \n{evectors}\nQH = \n{evectors.getH()}\nQH * Q = \n{np.dot(evectors.getH(), evectors)}')

#OUTPUT:
'''
Q =
[[ 0.84515425+0.j          0.50709255+0.16903085j]
 [-0.50709255+0.16903085j  0.84515425+0.j        ]]
QH =
[[ 0.84515425-0.j         -0.50709255-0.16903085j]
 [ 0.50709255-0.16903085j  0.84515425-0.j        ]]
QH * Q =
[[ 1.00000000e+00+0.00000000e+00j -1.12557096e-16-8.32667268e-17j]
 [-1.12557096e-16+8.32667268e-17j  1.00000000e+00+0.00000000e+00j]]
''' #diagonals are 1, rest is basically 0

# Showing the columns of a 4x4 fourier matrix are orthogonal

F = np.matrix([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])

print(f'4x4 fourier matrix F = \n{F}\nDot product of columns 1 and 2 = {np.inner(F[0], F[1])}'
f'\nDot product of columns 1 and 3 = {np.inner(F[0], F[2])}'
f'\nDot product of columns 1 and 4 = {np.inner(F[0], F[3])}'
f'\nDot product of columns 2 and 3 = {np.inner(F[1], F[2])}'
f'\nDot product of columns 2 and 4 = {np.inner(np.conj(F[1]), F[3])}'
f'\nDot product of columns 3 and 4 = {np.inner(F[2], F[3])}')

#OUTPUT:
'''
4x4 fourier matrix F =
[[ 1.+0.j  1.+0.j  1.+0.j  1.+0.j]
 [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]
 [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]
 [ 1.+0.j -0.-1.j -1.+0.j  0.+1.j]]
Dot product of columns 1 and 2 = [[0.+0.j]]
Dot product of columns 1 and 3 = [[0.+0.j]]
Dot product of columns 1 and 4 = [[0.+0.j]]
Dot product of columns 2 and 3 = [[0.+0.j]]
Dot product of columns 2 and 4 = [[0.+0.j]]
Dot product of columns 3 and 4 = [[0.+0.j]]
'''