# LECTURE 1 - The Geometry of Linear Equations

import numpy as np
from sympy import linear_eq_to_matrix, symbols
import ast

# System of 2 equations of the form A*x + B*y - C = 0

x, y = symbols('x y')
eqns = [2*x - y,
        -x + 2*y - 3] # = 0 is implied for these equations

tempA1, tempb1 = linear_eq_to_matrix(eqns, [x, y])

#converts MutableDenseMatrix returned by linear_eq_to_matrix to list that can be used in numpy array
def getAandb():
    tempA2 = str(tempA1); tempb2 = str(tempb1)
    tempA2 = tempA2[7:len(tempA2)-1]; tempb2 = tempb2[7:len(tempb2)-1]
    tempA2 = ast.literal_eval(tempA2); tempb2 = ast.literal_eval(tempb2)
    return tempA2, tempb2

# Now we use NumPy to solve for x in Ax = b, plugging in A and b from above

def getSolution():
    A = np.array(getAandb()[0])
    b = np.array(getAandb()[1])
    x = np.linalg.solve(A, b)
    for i in range(0, len(x)):
        if x[i] == -0:
            x[i] = 0
    return x

print(f'\nA solution to the system of 2 equations {eqns} is: \n{getSolution()} \n\n')

#OUTPUT:
'''
A solution to the system of 2 equations [2*x - y, -x + 2*y - 3] is: 
[[1.]
 [2.]]
'''


# System of 3 equations of the form A*x + B*y + C*z - D = 0; same as above but with the extra 'z'

x, y, z = symbols('x y z')
eqns = [2*x - y,
        -x + 2*y - z + 1,
        -3*y + 4*z - 4]

tempA1, tempb1 = linear_eq_to_matrix(eqns, [x, y, z])

print(f'A solution to the system of 3 equations {eqns} is: \n{getSolution()} \n\n')

#OUTPUT:
'''
A solution to the system of 3 equations [2*x - y, -x + 2*y - z + 1, -3*y + 4*z - 4] is: 
[[0.]
 [0.]
 [1.]]
'''

# Multiplication of matrices - NumPy makes it easy!

A = np.array([[2, 5],
              [1, 3]])
x = np.array([[1],
              [2]])

b = np.dot(A, x)

print(f'Matrix A: \n{A}, \nvector x: \n{x}, \nb = A*x = \n{b}')

#OUTPUT:
'''
Matrix A:
[[2 5]
 [1 3]],
vector x:
[[1]
 [2]],
b = A*x =
[[12]
 [ 7]]
'''