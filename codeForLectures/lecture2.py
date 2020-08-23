# LECTURE 2 - Elimination with Matrices

import numpy as np
from sympy import linear_eq_to_matrix, symbols
import ast

# System of 3 Equations of the form A*x + B*y + C*z - D = 0

# same as from lecture 2.. elimination is done behind the scenes
x, y, z = symbols('x y z')
eqns = [x + 2*y + z - 2,
        3*x + 8*y + z - 12,
        4*y + z - 2] # = 0 is implied for these equations

tempA, tempb = linear_eq_to_matrix(eqns, [x, y, z])

tempA = str(tempA); tempb = str(tempb)
tempA = tempA[7:len(tempA)-1]; tempb = tempb[7:len(tempb)-1]
tempA = ast.literal_eval(tempA); tempb = ast.literal_eval(tempb)

A = np.array(tempA)
b = np.array(tempb)
x = np.linalg.solve(A, b)

print(f'\nA solution to the system of 3 equations {eqns} is: \n{x} \n')

#OUTPUT:
'''
A solution to the system of 3 equations [x + 2*y + z - 2, 3*x + 8*y + z - 12, 4*y + z - 2] is:
[[ 2.]
 [ 1.]
 [-2.]]
'''

# System of 3 equations with 0 in pivot position and unable to exchange with another row

A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, -4]])
b = np.array([[2], [12], [2]])
x = np.linalg.solve(A, b)

print(f'\nA solution to the system of 3 equations with 0 in the pivot is: \n{x} \n..garbage answer, since this matrix is not invertible')

#OUTPUT:
'''
A solution to the system of 3 equations with 0 in the pivot is:
[[ 2.25179981e+16]
 [-7.50599938e+15]
 [-7.50599938e+15]]
..garbage answer, since this matrix is not invertible
'''

# Multiplying a matrix by the identity matrix

A = np.array(np.random.randint(1, 9, size = (3, 3)))
I = np.identity(3)

print(f'\nA = \n{A}, \nI = \n{I}, \nA * I = \n{np.matmul(A, I)}')

#OUTPUT:
'''
A =
[[8 2 2]
 [3 3 8]
 [6 6 2]],
I =
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]],
A * I =
[[8. 2. 2.]
 [3. 3. 8.]
 [6. 6. 2.]]
'''

# Associative Law of Matrices

A = np.array(np.random.randint(1, 9, size=(3, 3)))
B = np.array(np.random.randint(1, 9, size=(3, 3)))
C = np.array(np.random.randint(1, 9, size=(3, 3)))

print(f'\nA * (B * C) = \n{np.dot(A, np.dot(B, C))} \n(A * B) * C = \n {np.dot(np.dot(A, B), C)}\n')

#OUTPUT:
'''
A * (B * C) =
[[164 424 352]
 [151 446 448]
 [190 656 618]]
(A * B) * C =
 [[164 424 352]
 [151 446 448]
 [190 656 618]]
'''

# Permuting the rows of a 2x2 matrix

A = np.array([[1, 2], [3, 4]])

def permute(A):
    P = np.random.permutation(A)
    if (P == A).all():
        return permute(A)
    else:
        return P

print(f'A = \n{A}\nA after permuting rows = \n{permute(A)}\n')

#OUTPUT:
'''
A =
[[1 2]
 [3 4]]
A after permuting rows =
[[3 4]
 [1 2]]
'''

# Permuting the columns of a 2x2 matrix - method taken from https://stackoverflow.com/a/50381558/12733759
A = np.array([[5, 6], [2, 3]])

originalA = np.copy(A)

col1 = 0; col2 = 1
A.T[[col1, col2]] = A.T[[col2, col1]]

print(f'A = \n{originalA}\nA after permuting columns = \n{A}\n')

#OUTPUT:
'''
A =
[[5 6]
 [2 3]]
A after permuting columns =
[[6 5]
 [3 2]]
'''

# Showing matrices are not commutative by multiplication

A = np.array(np.random.randint(1, 9, size=(3, 3)))
B = np.array(np.random.randint(1, 9, size=(3, 3)))

print(f'A * B = \n{np.dot(A, B)}\nB * A = \n{np.dot(B, A)}')

#OUTPUT:
'''
A * B =
[[42 40 79]
 [29 28 53]
 [53 50 85]]
B * A =
[[ 62  24  42]
 [134  44  79]
 [ 82  27  49]]
'''