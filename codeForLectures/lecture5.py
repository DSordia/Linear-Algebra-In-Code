# LECTURE 5 - Transposes, Permutations, Spaces R^n

import numpy as np

# Showing P inverse = P transpose and P transpose * P = I

I = np.identity(3)
P = np.random.permutation(I)

print(f'I = \n{I}\nPermutation of I = \n{P}\nInverse of permutation = \n{np.round(np.linalg.inv(P), 2)}\nTranspose of permutation = \n{P.transpose()}\n'
f'P transpose * P = \n{np.dot(P.transpose(), P)}')

#OUTPUT:
'''
I =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Permutation of I =
[[0. 1. 0.]
 [1. 0. 0.]
 [0. 0. 1.]]
Inverse of permutation =
[[0. 1. 0.]
 [1. 0. 0.]
 [0. 0. 1.]]
Transpose of permutation =
[[0. 1. 0.]
 [1. 0. 0.]
 [0. 0. 1.]]
P transpose * P =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

# Transpose of a 3x4 matrix

A = np.array(np.random.randint(1, 9, size = (3, 4)))

print(f'A {A.shape} = \n{A}\nA transpose {A.transpose().shape} = \n{A.transpose()}')

#OUTPUT:
'''
A (3, 4) =
[[5 8 1 5]
 [5 2 5 3]
 [4 4 8 7]]
A transpose (4, 3) =
[[5 5 4]
 [8 2 4]
 [1 5 8]
 [5 3 7]]
'''

# Transpose of a symmetric matrix

A = np.array([[3, 1, 7], [1, 2, 9], [7, 9, 4]])

print(f'Symmetric matrix A = \n{A}\nTranspose of A = \n{A.transpose()}')

#OUTPUT
'''
Symmetric matrix A =
[[3 1 7]
 [1 2 9]
 [7 9 4]]
Transpose of A =
[[3 1 7]
 [1 2 9]
 [7 9 4]]
'''

# Transpose of R transpose * R where R is a rectangular matrix

R = np.array(np.random.randint(1, 9, size = (3, 4)))
RTranspose = R.transpose()

print(f'R = \n{R}\nR transpose * R = \n{np.dot(R, RTranspose)}')

# OUTPUT
'''
R =
[[4 8 5 5]
 [1 3 7 4]
 [8 2 4 1]]
R transpose * R =
[[130  83  73]
 [ 83  75  46]
 [ 73  46  85]]
'''