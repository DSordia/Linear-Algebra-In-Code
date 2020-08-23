# LECTURE 3 - Multiplication and Inverse Matrices

import numpy as np

# Multiplying two square matrices of the same size

A = np.array(np.random.randint(1, 9, size = (3, 3)))
B = np.array(np.random.randint(1, 9, size = (3, 3)))
AB = np.dot(A, B)

print(f'A {A.shape} = \n{A}\nB {B.shape} = \n{B}\nA * B {AB.shape} =\n{AB}\n')

#OUTPUT:
'''
A (3, 3) =
[[6 4 5]
 [5 2 4]
 [3 5 8]]
B (3, 3) =
[[7 8 3]
 [4 4 2]
 [1 8 6]]
A * B (3, 3) =
[[ 63 104  56]
 [ 47  80  43]
 [ 49 108  67]]
'''

A = np.array(np.random.randint(1, 9, size = (3, 3)))
B = np.array(np.random.randint(1, 9, size = (4, 4)))

# Multiplying two square matrices of different sizes

# print(f'A = \n{A}\nB = \n{B}\nA * B =\n{np.dot(A, B)}\n')

#OUTPUT:
'''
ValueError: shapes (3,3) and (4,4) not aligned: 3 (dim 1) != 4 (dim 0)
'''

# Multiplying two matrices A (m x n) and B (a x b) where n = a

A = np.array(np.random.randint(1, 9, size = (3, 4)))
B = np.array(np.random.randint(1, 9, size = (4, 5)))
AB = np.dot(A, B)

print(f'A {A.shape} = \n{A}\nB {B.shape} = \n{B}\nA * B {AB.shape} =\n{AB}\n')

#OUTPUT:
'''
A (3, 4) =
[[8 6 8 4]
 [3 4 7 2]
 [2 2 6 8]]
B (4, 5) =
[[2 4 4 2 4]
 [5 3 4 1 5]
 [4 5 2 1 2]
 [1 2 4 7 7]]
A * B (3, 5) =
[[ 82  98  88  58 106]
 [ 56  63  50  31  60]
 [ 46  60  60  68  86]]
'''

# Multiplying two matrices A (m x n) and B (a x b) where n does not equal a

A = np.array(np.random.randint(1, 9, size = (3, 4)))
B = np.array(np.random.randint(1, 9, size = (5, 4)))
#AB = np.dot(A, B)

# print(f'A {A.shape} = \n{A}\nB {B.shape} = \n{B}\nA * B {AB.shape} =\n{AB}\n')

#OUTPUT:
'''
ValueError: shapes (3,4) and (5,4) not aligned: 4 (dim 1) != 5 (dim 0)
'''

# Inverse of an invertible / non-singular matrix
A = np.array([[1, 3], [2, 7]])
Ainv = np.linalg.inv(A)

print(f'A = \n{A}\n A inverse = \n{Ainv}')

#OUTPUT:
'''
A =
[[1 3]
 [2 7]]
 A inverse =
[[ 7. -3.]
 [-2.  1.]]
'''

# Inverse of a non-invertible / singular matrix

A = np.array([[1, 3], [2, 6]])
#Ainv = np.linalg.inv(A)

#print(f'A = \n{A}\n A inverse = \n{Ainv}')

#OUTPUT:
'''
numpy.linalg.LinAlgError: Singular matrix
'''