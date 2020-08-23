# LECTURE 4 - Factorization into A = LU

import numpy as np
import time
import math

# Inverse of a product of matrices

A = np.array(np.random.randint(1, 5, size = (3, 3)))
B = np.array(np.random.randint(1, 5, size = (3, 3)))
AB = np.dot(A, B)

print(f'AB = \n{AB}\nAB inverse = \n{np.round(np.linalg.inv(AB), 2)}\n')

#OUTPUT:
'''
AB =
[[21 13 19]
 [19 11 18]
 [15 11 13]]
AB inverse =
[[ 2.75 -2.   -1.25]
 [-1.15  0.6   0.85]
 [-2.2   1.8   0.8 ]]
'''

# Transpose of the identity matrix

I = np.identity(3)

print(f'I = \n{I}\nI transpose = \n{I.transpose()}\n')

# OUTPUT:
'''
I =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
I transpose =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

# Transpose of a regular matrix

A = np.array(np.random.randint(1, 9, size = (3, 3)))

print(f'A = \n{A}\nA transpose = \n{A.transpose()}\n')

#OUTPUT:
'''
A =
[[6 8 7]
 [6 5 8]
 [4 7 3]]
A transpose =
[[6 6 4]
 [8 5 7]
 [7 8 3]]
 '''

# Inverse of the transpose of a matrix

A = np.array(np.random.randint(1, 9, size = (3, 3)))
Atranspose = A.transpose()

print(f'A = \n{A}\nA transpose = \n{Atranspose}\nInverse of A transpose = \n{np.round(np.linalg.inv(Atranspose), 2)}')

#OUTPUT:
'''
A =
[[7 7 8]
 [1 6 7]
 [7 6 4]]
A transpose =
[[7 1 7]
 [7 6 6]
 [8 7 4]]
Inverse of A transpose =
[[ 0.18 -0.45  0.36]
 [-0.2   0.28 -0.07]
 [-0.01  0.41 -0.35]]
 '''

 # Elimination on a 10000 x 10000 matrix

A = np.array(np.random.randint(1, 9, size = (10000, 10000)))
b = np.array(np.random.randint(1, 9, size = (10000, 1)))

def compute():
    x = np.linalg.solve(A, b)
    return x

#start_time = time.time()
#answer = compute()
#print(f'Took {time.time() - start_time} seconds to get the answer \n{answer}')

#OUTPUT:
'''
Took 11.965126276016235 seconds to get the answer
[[ 2.52340867]
 [-1.11230735]
 [-0.59473782]
 ...
 [ 0.3309872 ]
 [ 1.11759928]
 [-2.5100072 ]]
'''

# All row permutations of a 3x3 identity matrix

I = np.identity(3)
permutations = []
permutations.append(I)

def permute(A):
    P = np.random.permutation(A)
    if len(permutations) == math.factorial(3):
        return permutations
    for permutation in permutations:
        if (P == permutation).all():
            return permute(A)
    permutations.append(P)
    return permute(A)

permute(I)

print('All permutations of 3x3 Identity matrix: ')
for permutation in permutations:
    print(f'{permutation}\n')

#OUTPUT:
'''
All permutations of 3x3 Identity matrix: 
[[1. 0. 0.] 
 [0. 1. 0.] 
 [0. 0. 1.]]

[[0. 1. 0.]
 [1. 0. 0.]
 [0. 0. 1.]]

[[0. 1. 0.]
 [0. 0. 1.]
 [1. 0. 0.]]

[[0. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]]

[[0. 0. 1.]
 [1. 0. 0.]
 [0. 1. 0.]]

[[1. 0. 0.]
 [0. 0. 1.]
 [0. 1. 0.]]
'''

# Inverse and transpose of a permutation matrix

I = np.identity(3)
P = np.random.permutation(I)

print(f'I = \n{I}\nRandom permutation of I = \n{P}\nInverse of the permutation of I = \n{np.round(np.linalg.inv(P), 2)}\nTranspose of the permutation of I = \n{P.transpose()}')

#OUTPUT:
'''
I =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Random permutation of I =
[[0. 0. 1.]
 [1. 0. 0.]
 [0. 1. 0.]]
Inverse of the permutation of I =
[[0. 1. 0.]
 [0. 0. 1.]
 [1. 0. 0.]]
Transpose of the permutation of I =
[[0. 1. 0.]
 [0. 0. 1.]
 [1. 0. 0.]]
'''