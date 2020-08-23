# LECTURE 29 - Singular Value Decomposition

import numpy as np

# Showing that A = UEV^T for a 2x2 non-symmetric invertible matrix

A = np.array([[4, 4], [-3, 3]])

ATA = np.dot(A.transpose(), A)
AAT = np.dot(A, A.transpose())

evalues1, evectors1 = np.linalg.eig(ATA)
evalues2, evectors2 = np.linalg.eig(AAT)

E = np.array([[np.sqrt(evalues1[0]), 0], [0, np.sqrt(evalues1[1])]])

U = evectors2
VT = evectors1.transpose()

print(f'A = \n{A}\nUEV^T = \n{np.dot(U, np.dot(E, VT))}')

#OUTPUT:
'''
A =
[[ 4  4]
 [-3  3]]
UEV^T =
[[ 4.  4.]
 [-3.  3.]]
'''

# elegant way of doing SVD using NuMpy taken from https://stackoverflow.com/a/58523650/12733759
U, D, V = np.linalg.svd(A, full_matrices = False)
A_reconstructed = U @ np.diag(D) @ V
print(A_reconstructed)

#OUTPUT:
'''
[[ 4.  4.]
 [-3.  3.]]
'''

# Showing that A = UEV^T for a 2x2 non-invertible matrix

A = np.array([[4, 3], [8, 6]])

ATA = np.dot(A.transpose(), A)
AAT = np.dot(A, A.transpose())

evalues1, evectors1 = np.linalg.eig(ATA)
evalues2, evectors2 = np.linalg.eig(AAT)

E = np.array([[np.sqrt(evalues1[0]), 0], [0, np.round(np.sqrt(evalues1[1]))]])
U = evectors2
VT = evectors1.transpose()

print(f'A = \n{A}\nUEV^T = \n{np.dot(U, np.dot(E, VT))}')

#OUTPUT:
'''
A =
[[4 3]
 [8 6]]
UEV^T =
[[-8. -6.]
 [ 4.  3.]]
''' #note that these two matrices are the same.. multiply row 1 by -1 and flip rows 1 and 2; these are valid row operations

# elegant way of doing SVD using NuMpy taken from https://stackoverflow.com/a/58523650/12733759
U, D, V = np.linalg.svd(A, full_matrices = False)
A_reconstructed = U @ np.diag(D) @ V
print(A_reconstructed)

#OUTPUT:
'''
[[4. 3.]
 [8. 6.]]
'''